# Docker tutorial to create docker container
This tutorial will walk you through creating a docker container to use on CHTC. The idea of a docker container is to create an enclosed system of all your needed software and packages that can be pulled from docker hub and used anywhere. Most of you will need a docker just containing python and your needed python packages. This codebase has resources to create a docker container using an environment.yml file (conda) or requirements.txt.

### Download docker desktop for your specific os
Download link: https://www.docker.com/products/docker-desktop/

After downloading, open the application and create an account

### Create docker container with pip
1. Download docker_pip. This folder has a sample requirements.txt and the needed dockerfile. Once downloaded, navigate to the directory in your local terminal.
2. Edit the requirements.txt to include your needed versions or packages.
3. Edit the dockerfile to include any additional software you need. The current file installs wget, python3, pip, git, vim, and basic command line commands
4. In the directory on your local terminal run, changing docker_usrnm to your username from creating your docker account and container_name being the name you want to assign this container: docker build --platform=linux/amd64 -t docker_usrnm/container_name .



### Create docker container with conda
