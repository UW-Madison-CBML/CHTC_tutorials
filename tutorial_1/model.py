import tarfile
import pickle
import glob
import io
import sys
import matplotlib.pyplot as plt
import seaborn as sns
import random
import os
import pandas as pd
import numpy as np


#NEEDED FOR CHTC
os.environ["TORCHINDUCTOR_CACHE_DIR"] = "/tmp/torch_cache"
os.environ["USER"] = "researcher"
os.environ["LOGNAME"] = "researcher"

from torch.utils.data import Dataset, DataLoader
import torch.nn.functional as F
import torchvision.transforms.functional as TF
import torch
import torch.nn as nn
import torch.optim as optim

from torch.utils.data import DataLoader
from PIL import Image

import tifffile as tiff


# Helper functions
def get_random_patch(img, pad=50, patch_size=512):
    img_array = np.array(img)
    h, w = img_array.shape[:2] # 2048, 2048
    # Maximum possible top-left corner
    max_x = w - patch_size - pad
    max_y = h - patch_size - pad
    # Generate random coordinates
    x = random.randint(pad, max_x)
    y = random.randint(pad, max_y)
    # Crop the patch [y:y+h, x:x+w]
    patch = img_array[y:y+patch_size, x:x+patch_size]
    return patch

def rotate_patch(img_arr):
    rotations = []
    rotations.append(img_arr) #original
    tmp = np.rot90(img_arr)
    rotations.append(tmp) #90
    tmp = np.rot90(tmp)
    rotations.append(tmp) #180
    tmp = np.rot90(tmp)
    rotations.append(tmp) #270
    return rotations

def generate_images(img_path, save_path, pad=0, n_patches=10, seed=777):
    save = os.path.basename(img_path).replace('.tif', '')
    img = tiff.imread(img_path).astype(np.float32)
    max_val = 65535 if img.dtype == np.uint16 else 255
    img /= max_val
    random.seed(seed)
    for i in range(n_patches):
        tmp = get_random_patch(img, pad=pad) #(512,512)
        rots = rotate_patch(tmp) #(4,512,512)
        for a, image in enumerate(rots): #[0, 90, 180, 270]
            # Original
            save_name = f"{save_path}/{save}_p{i}_{a}.tif"
            tiff.imwrite(save_name, image)
            # Transpose h
            arr_h = np.flip(image, axis=0) #horizontal
            save_name = f"{save_path}/{save}_p{i}_{a}_h.tif"
            tiff.imwrite(save_name, arr_h)
            # Transpose v
            arr_v = np.flip(image, axis=1) #vertical
            save_name = f"{save_path}/{save}_p{i}_{a}_v.tif"
            tiff.imwrite(save_name, arr_v)

# Dataloader
class LoadImagePatches(Dataset):
    def __init__(self, 
                 image_dir):
        self.image_dir = image_dir
        self.filenames = [f for f in os.listdir(image_dir) if f.endswith(('.tif', '.tiff'))] # Filter for .tif or .tiff files
    def __len__(self):
        return len(self.filenames)
    def __getitem__(self, idx):
        img_path = os.path.join(self.image_dir, self.filenames[idx])
        img = tiff.imread(img_path).astype(np.float32)
        return torch.tensor(img).unsqueeze(0)

# Model
class ConvAutoencoder(nn.Module):
    def __init__(self):
        super(ConvAutoencoder, self).__init__()
        
        # Encoder
        self.encoder = nn.Sequential(
            nn.Conv2d(1, 16, kernel_size=3, stride=2, padding=1), 
            nn.ReLU(),
            nn.Conv2d(16, 32, kernel_size=3, stride=2, padding=1), 
            nn.ReLU()
        )
        
        # Decoder
        self.decoder = nn.Sequential(
            nn.ConvTranspose2d(32, 16, kernel_size=3, stride=2, padding=1, output_padding=1), 
            nn.ReLU(),
            nn.ConvTranspose2d(16, 1, kernel_size=3, stride=2, padding=1, output_padding=1), 
            nn.Sigmoid() # Use Sigmoid if input is normalized [0,1]
        )

    def forward(self, x):
        x = self.encoder(x)
        x = self.decoder(x)
        return x


# Variables
img_path = sys.argv[1]
output_dir = sys.argv[2]
n_epochs = int(sys.argv[3])
save_name = sys.argv[4]

# Create patches
img_files = glob.glob(f'{img_path}/*tif')

save_path = './patches/'
for img_path in img_files:
    generate_images(img_path, save_path, pad=50, n_patches=10, seed=7) 

# Load patches
torch.manual_seed(777)
dataset = LoadImagePatches(image_dir=save_path) 
loader = DataLoader(dataset, batch_size=64, shuffle=True)


################################################################
# Training
torch.cuda.empty_cache()

device = torch.device("cuda")
torch.manual_seed(777)

model = ConvAutoencoder().to(device)
criterion = nn.MSELoss()
optimizer = torch.optim.Adam(model.parameters(), lr=1e-4)

model.train()
for epoch in range(n_epochs): 
    for i, images in enumerate(loader):
        images = images.to(device)
        outputs = model(images)
        loss = criterion(outputs, images)
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
    print(f"Epoch {epoch+1}, Loss: {loss.item():.10f}")
    

save_path = f'./{output_dir}/{save_name}.pth'
torch.save({
    'epoch': n_epochs,
    'model_state_dict': model.state_dict(),
    'optimizer_state_dict': optimizer.state_dict(),
    'loss': loss
}, save_path)


################################################################
# Save a before and after
with torch.no_grad():
    # Grab the first image from the last batch
    original = images[0].cpu().squeeze()
    recon = outputs[0].cpu().squeeze()
    
    plt.figure(figsize=(10, 5))
    plt.subplot(1, 2, 1)
    plt.title("Original TIF")
    plt.imshow(original, cmap='gray')
    
    plt.subplot(1, 2, 2)
    plt.title("Model Reconstruction")
    plt.imshow(recon, cmap='gray')
    plt.savefig(f'./{output_dir}/{save_name}.pdf')

