# CHTC_tutorials
This repo is meant to help new CHTC users to start running their own jobs. Sample scripts are provided so the user just needs to edit as needed for basic job submissions.

Each folder in this repo contains it's own markdown file describing how to use each file and covers the most common job submission scenarios a new CHTC user may face.

### Descriptions
1. **docker**: How to create and push your own docker container
2. **general_scripts**: General use scripts covering both single job and multi-job submissions
3. **tutorial_1**: Simple tutorial walking through a simple job submission
4. **tutorial_2**: A more complex tutorial walking through a multi-job submission

# Basic CHTC commands
Here are some basic CHTC commands
|Command|Function|
|---|---|
|`get_quotas` | See your directory quotas after you have logged in|
|`condor_submit` submit.sub | Submit a job to the queue|
|`condor_q` | Check on your jobs (idle, running, hold)|
|`condor_q -hold` | Get explanation to why a job is on hold|
|`condor_rm <job_id>` | Remove job from queue|
|`condor_release <job_id>` | Release a job on hold to enter the queue again|
|`condor_ssh_to_job <job_id>` | Connect to the job and enter it|
