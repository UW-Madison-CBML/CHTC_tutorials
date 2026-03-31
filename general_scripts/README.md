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




# submit.sub


# python.py
This one's pretty explanatory. This will be the python script that runs your model, does analysis, etc
