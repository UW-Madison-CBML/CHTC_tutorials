# Tutorial 0: Use a trained model

This tutorial will walk you through how to take a current trained model `pth` and run inference with it. The main goal of this tutorial is to introduce you to the needed scripts needed to run a job on CHTC. For a more in depth tutorial, see tutorial_1.

Data provided in `tutorial_0_inputs.tar.gz` are SHG images from ([Keikhosravi et al., 2020)](https://www.nature.com/articles/s42003-020-01151-5).

For this tutorial you will need:
1. A [CHTC account](https://chtc.cs.wisc.edu/uw-research-computing/form)
2. `tutorial_0`
3. Basic understanding of command line
4. You **DO NOT** need to make a docker environment as we are using a premade one

The overall steps for this tutorial
1. Download `tutorial_0`
2. Move all files from your local device to CHTC
3. Submit job
4. Move `tutorial_0_output.tar.gz` from CHTC to your local device

## Download `tutorial_0`
1. Download this repo to your local device
```
git pull https://github.com/UW-Madison-CBML/CHTC_tutorials.git
```
2. In your terminal, navigate to `CHTC_tutorials/`
3. Type `ls` and hit enter. You should see `tutorial_0` listed

## Move `tutorial_0` to CHTC
1. We now want to move the entire `tutorial_0` directory to CHTC
2. Use this command on your local terminal, enter your password and follow the duo-push prompt (type `1` for push, otherwise enter code)
```
scp -r tutorial_0 net_id@ap200#.chtc.wisc.edu:/home/net_id
```
3. Now that the directory is on CHTC, open a new terminal window (`ctrl`+`n`) or tab (`ctrl`+`t`) and log into CHTC. Follow the prompts
```
ssh net_id@ap200#.chtc.wisc.edu
```
4. Once logged in, type `ls` and you should see `tutorial_0` listed

## Submit your job
1. `tutorial_0` contains everything you need to run your job

|File|Function|
|---|---|
|tutorial_0.pth|The trained model you are using|
|tutorial_0_inputs.tar.gz|Input files you are inputting into the model|
|submit_job.sub|Submit script, tells HTCondor which resources you want|
|run_inference.sh|Your executable used to run command line code|
|model_inference.py|Script for running the model inferece|

2. `cd` into `tutorial_0`. You should see all the files listed above
3. To submit your job run this command
```
condor_submit submit_job.sub
```
4. Now check that your code is running.
```
condor_q
```
You will see something like this. If the job is running `1` will be under `RUN`
```
-- Schedd: ap2001.chtc.wisc.edu : <128.105.68.112:9618?... @ 04/07/26 15:48:16
OWNER  BATCH_NAME    SUBMITTED   DONE   RUN    IDLE  TOTAL JOB_IDS
net_id tutorial_0   4/7  15:42      _      _      1      1 6009642.0

1 jobs; 0 completed, 0 removed, 1 idle, 0 running, 0 held, 0 suspended
```

5. Wait for your job to complete. Once completed type `ls`. You should now see a new file: `tutorial_0_outputs.tar.gz`

6. Now you will want to check to make sure your `tutorial_0_outputs.tar.gz` has actual output. Run:
```
tar tf tutorial_0_outputs.tar.gz
```
7. 

## Move your output
1. Now that you know you have your output, you can transfer it back to your local device to look at it. From your **local** terminal:
```
scp net_id@ap200#.chtc.wisc.edu:/home/net_id/tutorial_0/tutorial_0_outputs.tar.gz .
```
2. Follow the password and duo-push prompts
3. You should now have your output on your local device and ready for analysis!







