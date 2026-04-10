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
from torchvision.utils import save_image
import torch
import torch.nn as nn
import torch.optim as optim

from torch.utils.data import DataLoader
from PIL import Image

import tifffile as tiff


# Dataloader
class LoadImagesFull(Dataset):
    def __init__(self, image_dir):
        self.image_dir = image_dir
        self.filenames = [f for f in os.listdir(image_dir) if f.endswith(('.tif', '.tiff'))]
    def __len__(self):
        return len(self.filenames)
    def __getitem__(self, index):
        img_path = os.path.join(self.image_dir, self.filenames[index])
        img = tiff.imread(img_path)
        img = img.astype(np.float32) / 255.0
        img = torch.from_numpy(img)
        img = img.unsqueeze(0)
        return img

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

torch.cuda.empty_cache()
device = torch.device("cuda")

# Variables
img_path = sys.argv[1]
model_path = sys.argv[2]
output_dir = sys.argv[3]

################################################################
# Load images
torch.manual_seed(777)
dataset = LoadImagesFull(image_dir=img_path) 
loader = DataLoader(dataset, batch_size=4, shuffle=True) #only 10 images

# Load model
torch.manual_seed(777)

model = ConvAutoencoder().to(device)
checkpoint = torch.load(model_path, map_location=device)
model_weights = checkpoint["model_state_dict"]
model.load_state_dict(model_weights)
model.to(device)

# Inferencing
model.eval()
# Load images
dataset = LoadImagesFull(image_dir=img_path) #change to dataloader name
loader = DataLoader(dataset, batch_size=1)

c = 1
with torch.no_grad(): # Disable gradient calculation
    for i, images in enumerate(loader):
        images = images.to(device)
        predictions = model(images)

        probs = torch.sigmoid(predictions) # 0.0 to 1.0
        pred_mask = (probs > 0.52).float() # Prediction mask

        save_image(pred_mask, f"{output_dir}/mask_{i}.png")

        torch.cuda.empty_cache()

