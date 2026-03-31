# General scripts for CHTC
These scripts are meant to be generic templates and need to be edited to specific users
The two most common submission types are given here: one job submission, multi-job submission using text file

Jobs generally consist of these 3 files:
1. **submit.sub**: submit script used to tell HTCondor how many resources to allocate and which files to use
2. **run_script.sh**: Bash script used as your *executable* in the submit script
3. **python.py**: Python script that is specified to run using `run_script.sh`

Additional HTCondor commands and submit script entries can be found [here](https://htcondor.readthedocs.io/en/latest/)

# run_script.sh
This bash script is called your executable and will contain any cmd commands needed to run your script and save your output files. This file **always** starts with `#/bin/bash` at the top. Use the provided script as a template.

You will need to install any additional packages, load any API keys, run your script, and tar gzip your outputs directory. The outputs directory is needed to tell HTCondor to transfer your output back to the login node from the compute node (compute node is where all the compute stuff happens, login node is the node you login to).

At the start of your script, pip install any additional packages that are not in your docker container. If everything is in your container already, there's no need for this.
```
pip install torch==2.10.0
pip install librosa
```

Uncomment the following code in the executable if you wish to use [Weights & Biases](https://wandb.ai/site/) to track training statistics.
```
if [ -f "api_keys.txt" ]; then
    WB_KEY=$(tail -n 1 api_keys.txt)
    export WANDB_KEY=$WB_KEY
    echo "HuggingFace token loaded from api_keys.txt"
fi
```

You can add echo statements in the script as a way to debug or check any variable names
```
echo $variable1
echo "Running"
# Run script with variable1
echo "Done"
```

Run your python script (or any other scripts)
```
python python.py
```

Now that you have your output files, you need to tar gzip them in a `folder.tar.gz`
```
# Make new directory
mkidr outputs

# Move the output files into outputs dir (change file names as needed)
mv *txt *json mymodel.pth outputs

# Tar gzip the directory, HTcondor will then know to transer this back
tar -zcvf outputs.tar.gz outputs
```

Now that you have your executable written, you can move on to your submit script (`submit.sub`)

# submit.sub
This submit script is used to tell HTCondor exactly what it needs to run your job (scripts, container, resources, etc). **Aside from =, there should not be any spaces**

Starting from the top of the file, specify which container you want to use
```
Universe   = container
container_image = docker://usernm/container_name #docker://lsvaren/transformers
```

Specify what your executable is
```
Executable = run_script.sh
```

Specify which files you need. These files will be copied from your login node to the compute node that your job runs on. 
```
transfer_input_files = model_og.py,model.py,api_keys.txt,osdf:///chtc/staging/net_id/files.tar.gz
```

These lines of code are needed to let the scheduler (HTCondor) to transfer input files at the start of the job and to transfer output files after the job ends
```
should_transfer_files = YES
when_to_transfer_output = ON_EXIT
```

The following lines of code are what tell the scheduler what compute resources are needed. Uncomment as needed
```
# Uncomment these if you need gpus
#request_gpus = 1
#+WantGPULab = true
#+WantFlock = true
#+GPUJobLength = "long"
#gpus_minimum_memory = 35 GB

#Requirements = (Target.HasCHTCStaging == true)
Requirements = (Machine == "machine_name2000.chtc.wisc.edu") #Ask for Jay's gpu name
request_memory = 35 GB
#retry_request_memory = RequestMemory*2 #Retry with twice the memory if first job runs out of memory
request_disk = 70 GB
request_cpus = 1
```

Next, specify the batch name and your output files. These can be anything but will be how you identify the job when checking on it and how to find the corresponding output files (err, out, log).
```
batch_name = job_name
output = $(Cluster).out
error = $(Cluster).err
log = $(Cluster).log
```

Finally, use `queue` at the end of the script. The default `queue` specifies to run the executable once. If you want to run it 10 times, you would change it to `queue 10`

# python.py
This one's pretty explanatory. This will be the python script that runs your model, does analysis, etc

**Make sure all the paths and such are relative paths corresponding to the compute node**


# For multi-job submissions
There's a couple different situations where you might want to do a multi-job submission:
1. I want to run the same script with multiple different datasets (ie. train a model using 5 different datasets)
2. I have lots of inputs that need the same short analysis (ie. 1000 sequences all analyzed the same)

## Scenario 1
For the first scenario see `scenario_1/` for sample scripts. You will create a inputs.txt file where the text file contains the set of inputs needed for a pytohn script. 

Two changes needed to happen in your submit.sub file. In the following code, your python.py script requires 3 arguments. These 3 arguements are specified in a third file, inputs.txt
```
# Added to the submit script
arguments = $(arg1) $(arg2) $(arg3)
...
queue arg1, arg2, arg3 from inputs.txt
```

A sample inputs.txt file may look like this:
```
path/arg1_1.txt, arg2_1, arg3_1
path/arg1_2.txt, arg2_2, arg3_2
path/arg1_3.txt, arg2_3, arg3_3
```

## Scenario 2
For the second scenario see `scenario_2/` for sample scripts. This scenario is meant for if you have thousands of items (ie sequences) in one file that need to all be processed the same way (same script), and are each independent. Instead of processing them all sequentially, you can chunk these items into multiple files and process each chunk in parallel as it's own job.

First, chunk your one input file into multiple files which will result in files like this
```
chunk1.txt
chunk2.txt
chunk3.txt
chunk4.txt
chunk5.txt
```

Now in your submit script, you will make similar changes as in scenario 1 where inputs.txt has a list of your chunk files
```
# Added to the submit script
arguments = $(chunk)
...
queue chunk from inputs.txt
```


### Optional
If you have a lot of input files or the input files are very large files, you can also change `transfer_input_files` to specifically transfer the files in inputs.txt
```
transfer_input_files = $(arg1),$(arg3) # Scenario 1
transfer_input_files = $(chunk)        # Scenario 2
```



