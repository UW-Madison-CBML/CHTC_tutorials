# Interactive sessions on CHTC

Interactive sessions on CHTC are great when you want to work through some code to debug before launching a full job. Here, you will walk through a submit script for an interactive session and how to launch one on CHTC. It's assumed you already have some basic CHTC experience for this walkthrough. The difference between an interactive session and a normal CHTC job is that you are transported to the compute node when the job starts. Once on the compute node, you can code interactively within command line. When done, transfer any output files back to your `/staging/net_id`.

### What you need
* submit_interactive_job.sub
* Docker image you want to pull
* Any files you need for the job
* Code you want to run in command line
* staging directory

## 1. Prepare submit_interactive_job.sub
First thing you need to do is prepare `submit_interactive_job.sub`. This is pretty much the same script you would have for a normal CHTC job, except you don't specify an executable.
```
Universe   = container
# Edit this to your own docker image (can keep as is too)
container_image = docker://lsvaren/transformers
```
Next, you specify the input files you want to transfer with the job. Notice how we skipped over specifying an `executable`. We don't need one since you'll be executing the code yourself!
```
transfer_input_files = your_file.txt,your_dir
```
The remaining part of the script specifies resource requests the same as with running a normal CHTC job
```
request_gpus = 1
request_cpus = 1
request_memory = 25 GB
request_disk = 40 GB
+WantGPULab = true
+WantFlock = true


batch_name = interactive
output = $(Cluster).out
error = $(Cluster).err
log = $(Cluster).log

queue 
```

## 2. Submit submit_interactive_job.sub
Now that you have your `submit_interactive_job.sub` file, you can submit the job as an interactive session using `condor_submit` and the `-i` flag for "interactive"
```
condor_submit -i submit_interactive_job.sub
```
Once submitted you should see something like this:
```
Submitting job(s).
1 job(s) submitted to cluster 6009333.
Waiting for job to start...
```
## 3. Start coding interactively
Once your job has successfully started, you can now start coding. Now you can pip install any additional packages and run any commands you need to. You can navigate python by using these commands
```
# Start python
python

# Exit python
exit()
```

## 4. Save your needed output files
When you are done running your code, you need to manually save your outputs. One way you can do that is to copy your output files to your staging directory
```
cp -r output_files /staging/net_id
```

## 5. Exit the session
After transferring all your files back to the login node, you can now exit the interactive session by typing `exit`. You may need to do this a couple times to end other processes as well.

## 6. Check to make sure job is not on hold
Double check that your job is not on hold in the queue
```
condor_q
```
If you see your interactive job sitting in the queue still, remove it
```
condor_rm <job_id>
```







