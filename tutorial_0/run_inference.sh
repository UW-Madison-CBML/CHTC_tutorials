#/bin/bash

##### Additional packages needed not in your docker container yet
pip install torch==2.10.0
pip install torchvision==0.25.0
pip install tifffile
pip install pillow
pip install matplotlib
pip install seaborn

# Unzip input image files
echo "unzip"
tar -zxf tutorial_0_inputs.tar.gz

# Assign variables
img_path='./tutorial_0_inputs/'
model_path='./tutorial_0.pth'
output_dir='./tutorial_0_outputs/'

mkdir $output_dir

# Run script using variables
echo "Running"
python model_inference.py $img_path $model_path $output_dir

# tar.gz the output directory
tar -zcvf tutorial_0_outputs.tar.gz tutorial_0_outputs

echo "DONE"
