# Tutorial 1
This will be an extensive tutorial to walk you through creating scripts to train a basic model and save the results. We will walk through step by step how to move files from your local computer to the CHTC, submit a job, and move results back to your local computer.

For this tutorial you will need:
1. A [CHTC account](https://chtc.cs.wisc.edu/uw-research-computing/form)
2. The `train_model_tutorial_1.py` script
3. VIM editor on your local device
4. Basic understanding of command line
5. You **DO NOT** need to make a docker environment as we are using a premade one

The overall steps for this tutorial
1. Download `train_model_tutorial_1.py`
2. Create `run_script.sh` and `submit_job.sub`
3. Prepare directory on CHTC
4. Move `train_model_tutorial_1.py`, `run_script.sh` and `submit_job.sub` from your local device to CHTC
5. Submit job
6. Move `tutorial_1_output.tar.gz` from CHTC to your local device

## 1. Download `train_model_tutorial_1.py`
1. Open your terminal on your local device and navigate to where you want to make a directory for this tutorial
2. Create a new directory named `tutorial_1`:

```mkdir tutorial_1```

3. Move into the directory: `cd tutorial_1`

4. Download `train_model_tutorial_1.py` from this folder and move it to your `tutorial_1` directory

This python file contains the code required for training our model and will be run using `run_script.sh`. We will make `run_script.sh` next...


## 2. Prepare `run_script.sh` and `run_script.sh`
### `run_script.sh`
1. Open a new file with vim named `run_script.sh`
   
```vi run_script.sh```

2. Enter 'insert' mode by pressing `i`. You should see `-- INSERT --` in the bottom left corner of your screen.
3. Type this as the first line at the very top of your file. Then hit `enter` 2 times to move down 2 lines.
```
#/bin/bash
```
4. Our docker container doesn't have `torch` so we need to `pip` install it. Type this on a new line in your file. Hit `enter` 2 more times.
```
#/bin/bash

pip install torch==2.10.0
```
6. So we know that our script started, add `echo "Starting script"` to a new line. Hit `enter` 2 more times.
```
#/bin/bash

pip install torch==2.10.0

echo "Starting script"
```
7. Now its time to actually train our model using `train_model_tutorial_1.py`. Add `python train_model_tutorial_1.py` the new line. Hit `enter` 2 more times.
```
#/bin/bash

pip install torch==2.10.0

echo "Starting script"

python train_model_tutorial_1.py
```
8. After our script is done running, it will save the model as `tutorial_1_model.pth`. We need to put that into a directory to tar gzip it. Make an output directory, move your output file (`tutorial_1_model.pth`) into the new directory and tar gzip it. Hit `enter` 2 more times.

```
#/bin/bash

pip install torch==2.10.0

echo "Starting script"

python train_model_tutorial_1.py

mkdir tutorial_1_output # Make output dir
mv tutorial_1_model.pth tutorial_1_output # Move output file into new dir
tar -zcvf tutorial_1_output.tar.gz tutorial_1_output # tar gzip dir
```

8. Now add  to let you know the script finish running and the directory was successfully tar gzipped
```
#/bin/bash

pip install torch==2.10.0

echo "Starting script"

python train_model_tutorial_1.py

mkdir tutorial_1_output # Make output dir
mv tutorial_1_model.pth tutorial_1_output # Move output file into new dir
tar -zcvf tutorial_1_output.tar.gz tutorial_1_output # tar gzip dir

echo "Done"
```

9. That's it for `run_script.sh`! Now you just need to save it by hitting `esc` (the `-- INSERT --` should disappear) and then typing `:wq`. Then hit `enter`.
10. You should now be back in your `tutorial_1` directory.
11. Check to make sure `run_script.sh` saved by typing `ls` and hitting `enter`.

### `run_script.sh`



## 3. Prepare directory on CHTC


## 4. Move files from local to CHTC

## 5. Submit job

## 6. Move tutorial_1_output.tar.gz from CHTC to local device













