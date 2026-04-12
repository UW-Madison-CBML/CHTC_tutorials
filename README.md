# CHTC_tutorials
This repo is meant to help new CHTC users to start running their own jobs. Sample scripts are provided so the user just needs to edit as needed for basic job submissions.

Each folder in this repo contains it's own markdown file describing how to use each file and covers the most common job submission scenarios a new CHTC user may face.

### Descriptions
1. **docker**: How to create and push your own docker container
2. **general_scripts**: General use scripts covering both single job and multi-job submissions
3. **tutorial_0**: Learn how to use a trained model (`.pth` not huggingface)
4. **tutorial_1**: Learn how to train a model 
5. **tutorial_2**: Learn how to do a multi-job submission `**NOT DONE**`

# Helpful links
Request a CHTC account [here](https://chtc.cs.wisc.edu/uw-research-computing/form.html)

Request a staging directory **or** a quota change [here](https://chtc.cs.wisc.edu/uw-research-computing/quota-request#how-to-check-your-quotas)

General CHTC guides [here](https://chtc.cs.wisc.edu/uw-research-computing/htc/guides)

[Dockerhub](https://hub.docker.com/)

[HTCondor documentation](https://htcondor.readthedocs.io/en/latest/)

[VIM documentation](https://www.vim.org/docs.php)

# Basic CHTC commands
Here are some basic CHTC commands
|Command|Function|
|---|---|
|`get_quotas` | See your directory quotas after you have logged in|
|`condor_submit submit.sub` | Submit a job to the queue|
|`condor_submit -i submit.sub` | Submit an interactive job|
|`condor_q` | Check on your jobs (idle, running, hold)|
|`condor_q -hold` | Get explanation to why a job is on hold|
|`condor_rm <job_id>` | Remove job from queue|
|`condor_release <job_id>` | Release a job on hold to enter the queue again|
|`condor_ssh_to_job <job_id>` | Connect to the job and enter it|

# Helpful commandline
Transfer files or directory from **CHTC to local**
```
# File
scp net_id@ap200#.chtc.wisc.edu:/path/to/file.txt . #current directory

# Directory
scp -r net_id@ap200#.chtc.wisc.edu:/path/to/dir_chtc .
```

Transfer files or directory from **local to CHTC**
```
# File
scp file.txt net_id@ap200#.chtc.wisc.edu:/path/to/dir_chtc

# Directory
scp -r dir_local net_id@ap200#.chtc.wisc.edu:/path/to/dir_chtc
```

Other helpful commands to navigate command line

|Command|Function|
|---|---|
|`ls`|list files in current directory|
|`ll`|list files with additional information (time, size, etc)|
|`pwd`|get absolute path of current directory|
|`cd /path/to/directory`|navigate to new directory|
|`mv file.txt /path/to/move/to`|move file.txt to /path/to/move/to|
|`mv file.txt file_new.txt`|rename file.txt to file_new.txt (also applicable to directories)|
|`cd file.txt file_copy.txt`|copy file.txt to file_copy.txt (also applicable to directories)|
|`mkdir new_dir`|create new directory in current directory|
|`rm file.txt`|remove file.txt|
|`rmdir directory`|remove directory (has to be empty)|
|`du -sh directory`|get size of directory|


# Helpful VIM
VIM is a common text editor used to edit files within command line. [Here](https://vim-adventures.com/) is a fun game to practice VIM commands.
|Command|Function|
|---|---|
|`vi file.txt`|open up file.txt in the editor|
|`i`|'insert' to be able to start editing the file|
|`dd`|delete the current line|
|`esc`+`:q`|exit editor after making **NO** changes|
|`esc`+`:q!`|exit editor and discard any changes made|
|`esc`+`:wq`|exit editor and save file after making changes|



