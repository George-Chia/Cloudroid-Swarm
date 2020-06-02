FROM ros:indigo
RUN apt-get clean
RUN apt-get update
RUN apt-get install -y g++

RUN apt-get update && apt-get install -y ros-indigo-rosbridge-server ros-indigo-slam-gmapping

RUN apt-get install vim-gtk -y
EXPOSE 9090