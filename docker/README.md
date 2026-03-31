# Walkthrough to create docker container
This tutorial will walk you through creating a docker container to use on CHTC. The idea of a docker container is to create an enclosed system of all your needed software and packages that can be pulled from docker hub and used anywhere. Most of you will need a docker just containing python and your needed python packages. This codebase has resources to create a docker container using an environment.yml file (conda) or requirements.txt.

### Download docker desktop for your specific os
Download docker desktop from [here](https://www.docker.com/products/docker-desktop/)

After downloading, open the application and create an account. You can now log into [Docker Hub](https://hub.docker.com/explore). In Docker Hub, you can check that your containers were pushed and look for pre-existing docker images.

### Prepare dockerfile with pip
1. Download `docker_pip`. This folder has a sample `requirements.txt` and the needed dockerfile. Once downloaded, navigate to the directory in your local terminal.
2. Edit the `requirements.txt` to include your needed versions or packages (versions can also be left off)
3. Edit the dockerfile to include any additional software you need. The current file installs everything you need for a basic python environment (wget, python3, pip, git, vim, and basic command line commands)


### Create dockerfile with conda
1. Download `docker_conda`. This folder has a sample `environment.yml` and the needed dockerfile. Once downloaded, navigate to the directory in your local terminal.
2. Edit the `environment.yml` to include your needed versions or packages. If you want to generate your own `environment.yml` file from a conda environment, follow steps 3-4. Otherwise move to step 5.
3. To generate your own `environment.yml`, activate your conda environment locally with `conda activate conda_env`
4. Once activated, run this in command line

```conda env export --from-history > environment.yml```

5. Edit the dockerfile to include any additional software you need. The current file installs everything you need for a basic conda environment with python (miniconda, wget, python3, pip, git, vim, and basic command line commands)

### Create and push the docker containter
1. In the directory on your local terminal run, changing `docker_usrnm` to your username from creating your docker account and `container_name` being the name you want to assign this container.

```docker build --platform=linux/amd64 -t docker_usrnm/container_name .```

2. Debug any errors that prevent the container from being created.
3. A successful container creation will end with `View build details: docker-desktop://dashboard/build/desktop-linux/desktop-linux/blah-blah-blah`
4. Now you have created a docker container locally and need to push it to Docker Hub
5. Open docker desktop
6. Navigate to the "images" tab on the lefthand side. Here you will see your local images
7. Find the one you want to push and click on the 3 vertical dots on the righthand side
8. Select "Push to Docker Hub". Depending on how large your container is, this may take a while
9. Once an image is pushed successfully, you can delete it from your local device (I suggest this because they take up a lot of storage)
