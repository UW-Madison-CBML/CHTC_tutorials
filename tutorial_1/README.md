# Tutorial 1
This will be an extensive tutorial to walk you through creating scripts to train a basic model and save the results. We will walk through step by step how to move files from your local computer to the CHTC, submit a job, and move results back to your local computer.

For this tutorial you will need:
1. A [CHTC account](https://chtc.cs.wisc.edu/uw-research-computing/form)
2. The `train_model_tutorial_1.py` script
3. VIM editor on your local device
4. Basic understanding of command line
5. You **DO NOT** need to make a docker environment as we are using a premade one

The overall steps for this tutorial
1. Download `train_model_tutorial_1.py`, and `tutorial_1_inputs`
2. Create `run_script.sh` and `submit_job.sub`
3. Move all files from your local device to CHTC
4. Submit job
5. Move `tutorial_1_output.tar.gz` from CHTC to your local device

## 1. Download `train_model_tutorial_1.py` and other files
1. Open your terminal on your local device and navigate to where you want to make a directory for this tutorial
2. Create a new directory named `tutorial_1`:

```mkdir tutorial_1```

3. Move into the directory: `cd tutorial_1`

4. Download `train_model_tutorial_1.py` from this folder and move it to your `tutorial_1` directory
5. Now also download `tutorial_1_inputs`. These are the files we will be using as input to train our model
6. Move `tutorial_1_inputs` to `tutorial_1` as well

This python file contains the code required for training our model and will be run using `run_script.sh`. We will make `run_script.sh` next...


## 2a. Prepare `run_script.sh`
1. Open a new file with VIM named `run_script.sh`
```
vi run_script.sh
```

2. Enter 'insert' mode by pressing `i`. You should see `-- INSERT --` in the bottom left corner of your screen
3. Type this as the first line at the very top of your file. Then hit `enter` 2 times to move down 2 lines
```
#/bin/bash
```
4. Our docker container doesn't have `torch` so we need to `pip` install it. Type this on a new line in your file. Hit `enter` 2 more times
```
#/bin/bash

pip install torch==2.10.0
```
6. So we know that our script started, add `echo "Starting script"` to a new line. Hit `enter` 2 more times
```
#/bin/bash

pip install torch==2.10.0

echo "Starting script"
```
7. Now its time to actually train our model using `train_model_tutorial_1.py`. Add `python train_model_tutorial_1.py` the new line. Hit `enter` 2 more times
```
#/bin/bash

pip install torch==2.10.0

echo "Starting script"

python train_model_tutorial_1.py
```
8. After our script is done running, it will save the model as `tutorial_1_model.pth`. We need to put that into a directory to tar gzip it. Make an output directory, move your output files (`tutorial_1_model.pth`, `tutorial_1_model.pkl`) into the new directory and tar gzip it. Hit `enter` 2 more times

```
#/bin/bash

pip install torch==2.10.0

echo "Starting script"

python train_model_tutorial_1.py

mkdir tutorial_1_output # Make output dir
mv tutorial_1_model.pth tutorial_1_model.pkl tutorial_1_output # Move output file into new dir
tar -zcvf tutorial_1_output.tar.gz tutorial_1_output # tar gzip dir
```

8. Now add  to let you know the script finish running and the directory was successfully tar gzipped
```
#/bin/bash

pip install torch==2.10.0

echo "Starting script"

python train_model_tutorial_1.py

mkdir tutorial_1_output # Make output dir
mv tutorial_1_model.pth tutorial_1_model.pkl tutorial_1_output # Move output file into new dir
tar -zcvf tutorial_1_output.tar.gz tutorial_1_output # tar gzip dir

echo "DONE"
```

9. That's it for `run_script.sh`! Now you just need to save it by hitting `esc` (the `-- INSERT --` should disappear) and then typing `:wq`. Then hit `enter`.
10. You should now be back in your `tutorial_1` directory.
11. Check to make sure `run_script.sh` saved by typing `ls` and hitting `enter`.

## 2b. Prepare `submit_job.sub`
Now we will create the submit script needed to execute our executable: `run_script.sh`

1. Using VIM again, open a new file named `submit_job.sub`
2. Type `i` to enter 'insert' mode
3. First, we specify our environment we want to run our script in is a container and then specify the docker container we want to pull from Docker Hub
```
Universe = container
container_image = docker://lsvaren/transformers
```
4. Next, we specify our executable
```
Executable = run_script.sh
```

5. Now we need to tell HTCondor which files we want to transfer to the job. Pay attention to **no spaces** between the commas
```
transfer_input_files = train_model_tutorial_1.py,tutorial_1_inputs
```
6. We want to specify to transfer input files to the job at the start of our job and transfer our output file back to your directory at the end of the job
```
should_transfer_files = YES
when_to_transfer_output = ON_EXIT
```
7. We want to allocate 1 GPU and 1 CPU as well as an amount of memory and disk space. Add `+WantGPULab = true` and `+WantFlock = true` for good measure.
```
request_gpus = 1
request_cpus = 1
request_memory = 25 GB
request_disk = 40 GB
+WantGPULab = true
+WantFlock = true
```

8. **Optional** Specify a specific machine to use
```
Requirements = (Machine == "machine_name2000.chtc.wisc.edu") #Ask for Jay's gpu name
```
9. Now give the job a name and specify your .out, .err, .log output files 
```
batch_name = tutorial_1
output = $(Cluster).out
error = $(Cluster).err
log = $(Cluster).log
```
10. Add `queue` on the last line

11. Save your edits. Hit `esc` and then type `:wq`
12. You should now be back in your `tutorial_1` directory
13. Check to make sure `submit_job.sub` saved by typing `ls` and hitting `enter`. You should see all your files listed

## 3. Move files to 
Now we will move all our files to CHTC so we can run them there. We will do this by copying the entire `tutorial_1` directory to your home directory on CHTC
1. Log into CHTC, entering your password and duo-push
```
ssh net_id@ap200#.chtc.wisc.edu
```
2. Type `pwd` and hit `enter`. You should see `/home/net_id`
3. Check your quota space by typing `get_quotas` and hit `enter
4. Open a new terminal window (you now have 2 windows) and navigate to where you have your `tutorial_1` directory with all the files but **do not** enter it
5. Type `ls` and make sure you see `tutorial_1` in your output list of files and directories. If you only see your files you just made, move out of the directory (`cd ../`)
6. Now copy `tutorial_1` to CHTC using `scp`, using `-r` to specify it's a directory
```
scp -r tutorial_1 net_id@ap200#.chtc.wisc.edu:/home/net_id
```
7. You will be prompted for password and duo-push
8. Move back to your CHTC terminal window
9. Type `ls` to check that `tutorial_1` transferred properly

## 5. Submit job
Now that all your necessary files are on CHTC, we can submit the job and train our model!
1. `cd tutorial_1`
2. `ls` to check all your files are there
3. Submit your job to queue
```
condor_submit submit_job.sub
```
4. After submitting to queue, you should see:
```
Submitting job(s).
1 job(s) submitted to cluster 6005849.
```
5. Now we want to check on our job and see if it's started running
```
condor_q
```
6. You should see something like this. If the job is running, `RUN` will have `1` beneath it instead of `IDLE`. Depending on how busy the queue is, it may take some time for the job to run. You can keep checking it's status using `condor_q`
```
OWNER  BATCH_NAME    SUBMITTED   DONE   RUN    IDLE  TOTAL JOB_IDS
net_id tutorial_1    3/31 10:02    _      _      1      1 6005850.0
```
7. Once your job is done running, it will disappear from the `condor_q` output
8. `ls` to list files in `tutorial_1`. You should now see `tutorial_1_output.tar.gz`
9. Check to make sure `tutorial_1_output.tar.gz` has our output
```
tar tf tutorial_1_output.tar.gz

# Expected output
tutorial_1_model.pth
tutorial_1_model.pkl
```
10. Check the .err file for any errors. There may be some warnings that appear and those should be ok. Debug if there are any major errors
```
# Show last 10 lines of file
tail *err
```
11. Check the output file as well. You want to see `DONE` at the very last line. This is from our `echo "DONE"` statement we added to `run_script.sh`
12. After checking to make sure everything ran ok, we can now transfer our `tutorial_1_output.tar.gz` back to our local device to look at


## 6. Move tutorial_1_output.tar.gz from CHTC to local device
1. Move back to your local terminal window
2. Navigate to `tutorial_1`
3. Move tutorial_1_output.tar.gz from CHTC to local
```
scp net_id@ap200#.chtc.wisc.edu:/home/net_id/tutorial_1/tutorial_1_output.tar.gz .
```
4. You will be prompted for your password and duo-push
5. Now we can unzip our files on our local device to analyze
```
tar -xvzf tutorial_1_output.tar.gz
```
6. You have now successfully created your own executable (`run_script.sh`), submit script (`submit_job.sub`), trained and saved your own model (`tutorial_1_model.pth`, `tutorial_1_model.pkl`)
