#/bin/bash

# pip install torch==2.10.0
# pip install librosa
# pip install wandb


# if [ -f "api_keys.txt" ]; then
#     WB_KEY=$(tail -n 1 api_keys.txt)
#     export WANDB_KEY=$WB_KEY
#     echo "HuggingFace token loaded from api_keys.txt"
# fi

echo "unzip"
tar -zxf google_birds.tar.gz

echo "move to one directory"
cd google_birds 
mv */*wav .
cd ../

echo "Running"

# basename="/staging/svaren/google_lstm/all_birds"
# savename="${basename}.pth"
# pklname="${basename}.pkl"

# wavfiles="./google_birds/"

# echo $basename
# echo $savename
# echo $pklname
# echo ""
# echo $wavfiles

python model.py #$wavfiles $savename $pklname
#python model_og.py

tar -zcvf test_birds.tar.gz test_birds

echo "DONE"
