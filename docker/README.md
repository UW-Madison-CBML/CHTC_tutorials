# Docker tutorial to create docker container
This tutorial will walk you through creating a docker container to use on CHTC. The idea of a docker container is to create an enclosed system of all your needed software and packages that can be pulled from docker hub and used anywhere. Most of you will need a docker just containing python and your needed python packages. This codebase has resources to create a docker container using an environment.yml file (conda) or requirements.txt.

### Download docker desktop for your specific os
Download docker desktop from [here](https://www.docker.com/products/docker-desktop/)

After downloading, open the application and create an account. You can now log into [dockerhub](https://hub.docker.com/explore). In dockerhub, you can check that your containers were pushed and look for pre-existing docker images.

### Create docker container with pip
1. Download `docker_pip`. This folder has a sample `requirements.txt` and the needed dockerfile. Once downloaded, navigate to the directory in your local terminal.
2. Edit the `requirements.txt` to include your needed versions or packages (versions can also be left off)
3. Edit the dockerfile to include any additional software you need. The current file installs everything you need for a basic python environment (wget, python3, pip, git, vim, and basic command line commands)
4. In the directory on your local terminal run, changing `docker_usrnm` to your username from creating your docker account and `container_name` being the name you want to assign this container

    ```docker build --platform=linux/amd64 -t docker_usrnm/container_name .```

5. Continue to **Push to dockerhub**

### Create docker container with conda
1. Download `docker_conda`. This folder has a sample `environment.yml` and the needed dockerfile. Once downloaded, navigate to the directory in your local terminal.
2. Edit the `environment.yml` to include your needed versions or packages. If you want to generate your own `environment.yml` file from a conda environment, follow steps 3-5. Otherwise move to step 6.
3. To generate your own `environment.yml`, activate your conda environment locally with `conda activate conda_env`
4. Once activated, run this in command line

   ```conda env export --from-history > environment.yml```

5. Edit the dockerfile to include any additional software you need. The current file installs everything you need for a basic conda environment with python (miniconda, wget, python3, pip, git, vim, and basic command line commands)
6. In the directory on your local terminal run, changing `docker_usrnm` to your username from creating your docker account and `container_name` being the name you want to assign this container

    ```docker build --platform=linux/amd64 -t docker_usrnm/container_name .```

7. Continue to **Push docker**


### Push to dockerhub
