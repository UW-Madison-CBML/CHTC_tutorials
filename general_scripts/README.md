# General scripts for CHTC
These scripts are meant to be generic templates and need to be edited to specific users
The two most common submission types are given here: one job submission, multi-job submission using text file

Jobs generally consist of these 3 files:
1. **submit.sub**: submit script used to tell HTCondor how many resources to allocate and which files to use
2. **run_job.sh**: Bash script used as your *executable* in the submit script
3. **python.py**: Python script that is specified to run using `run_job.sh`

Additional HTCondor commands and submit script entries can be found [here](https://htcondor.readthedocs.io/en/latest/)

# submit.sub




# run_job.sh



# python.py
This one's pretty explanatory. This will be the python script that runs your model, does analysis, etc
