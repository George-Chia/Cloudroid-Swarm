# Cloudroid Swarm
## Introduction
Cloudroid Swarm is a cloud robotic platform which supports the direct deployment of ROS software packages onto the cloud. Basically, it can be regarded as a PAAS platform which adopts the ROS application model. A ROS package can be covnerted into a cloud service automatically. The robotic applications can access the cloud service remotely in an on-demand style through a WebSocket protocol.

The service access is purely based on a cloud service paradigm, which means that you need not concern ROS master and other configurations. Multiple robots can access a service simultaneously, for example, to build their own map respectively. The robotic apllications which access the cloud services also need no modification, because Cloudrid can generate a stub ROS package with the same interface of the original ROS package, which acts as a local proxy of the remote cloud service.

By adopting kubernetes and docker container technology in the back-end, a ROS package which is orignally designed for a single robot can serve multiple robots simultaneously by dynamically instantiation of the servant in the cloud. And by specifying the resource demand of the ROS package (e.g., mem, CPU, etc.), the quaility of a service can be assured by the internal mechanisms of Cloudroid.

Please contact us through dingbo@nudt.edu.cn or yuanzhaozhai@126.com. Any feedback would be greatly appreciated.


## Build Cloudroid Swarm
Cloudroid Swarm is built and tested on Ubuntu 18.04, ROS melodic, but it's easy to migrate to other versions.

1. Since it currently based on kubernetes and Docker, Docker must be installed on each host nodes, and kubernetes must be deployed in the cluster.

2. Add user to the Docker group, then restart the Docker engine:

```bash
    sudo addgroup $USER docker
```

3. Setup the local registry in the cloud server:

```bash
    docker run -d -p 5000:5000 --restart=always --name registry registry:2
```

4. Install python components and other dependencies:

```bash
    sudo apt-get update
    sudo apt-get install python-dev python-pip python-tk git zip unzip
    sudo pip install pip --upgrade
```

5. In the root directory of Cloudroid project, install other python requirements:

```bash
    cd Cloudroid_Swarm/
    sudo pip install -r requirements.txt
```

6. Build the base ros image from the `base-image` directory, push it to the local docker registry:

```bash
    cd Cloudroid_Swarm/base-image/
    docker build .
    docker tag $(docker images -q | head -n1) ros:my
    docker tag ros:my localhost:5000/ros:my
    docker push localhost:5000/ros:my
```

7. Initialise the database. You need to create a database named cloudroid first.

```bash
    cd Cloudroid_Swarm/database
    mysql -u$USERNAME -pPASSWORD -Dcloudroid ./create_cloudroid_tables.sql
```


8. Run Cloudroid Swarm server:

```bash
    cd ..
    python run.py
```

Updated setting.html by Shuxiao on July 29, 2020.
