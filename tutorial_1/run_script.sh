#/bin/bash

##### Additional packages needed not in your docker container yet
pip install torch==2.10.0
pip install tifffile
pip install torchvision
pip install torch-topological
pip install pillow


##### Add any needed 
echo "unzip"
tar -zxf google_birds.tar.gz

echo "move to one directory"

mkdir tutorial_1_outputs
mkdir patches

echo "Running"

img_path='./tutorial_1_inputs/'
output_dir='./tutorial_1_outputs/'
n_epochs=50
save_name='tutorial_1_inputs_model'

python model.py $img_path $output_dir $n_epochs $save_name


tar -zcvf tutorial_1_outputs.tar.gz tutorial_1_outputs

echo "DONE"
