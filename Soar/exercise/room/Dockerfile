FROM stereolabs/zed:4.0-py-runtime-jetson-jp5.1.1

ENV DEBIAN_FRONTED=noninteractive
# NO INTERACTIVE ACTION DURING PACKAGE INSTALL

WORKDIR /usr/src/app

RUN apt-get update
RUN apt-get install -y build-essential
RUN apt-get install -y wget 
RUN apt-get install -y sudo
RUN apt-get install -y cmake 
RUN apt-get install -y python3 
RUN apt-get install -y python3-pip 
RUN apt-get install -y python3-numpy 
RUN apt-get install -y libopencv-dev 
RUN apt-get install -y python3-opencv 





RUN sudo adduser soar
RUN sudo usermod -aG sudo soar

RUN sudo apt update && sudo apt install locales
RUN sudo locale-gen en_US en_US.UTF=8
RUN sudo update-locale LC_ALL=en_US.UTF-8 LANG=en_US.UTF-8
RUN export LANG=en_US.UTF-8

RUN locale

RUN sudo apt update && sudo apt install curl gnupg2 lsb-release -y
RUN sudo sudo curl -sSL https://raw.githubusercontent.com/ros/rosdistro/master/ros.key  -o /usr/share/keyrings/ros-archive-keyring.gpg


RUN sudo sh -c 'echo "deb [arch=$(dpkg --print-architecture)] http://packages.ros.org/ros2/ubuntu $(lsb_release -cs) main" > /etc/apt/sources.list.d/ros2-latest.list'
RUN sudo apt update
RUN sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys F42ED6FBAB17C654
RUN sudo apt install ros-foxy-desktop -y \
ros-foxy-rmw-fastrtps*

RUN sudoudo apt install -y python3-pip
RUN pip3 install -U argcomplete

RUN sudo apt update
RUN sudo apt install python3-colcon-common-extensions
RUN source /opt/ros/foxy/setup.bash
RUN mkdir -p ~/gcamp_ros2_ws/src
RUN cd ~/gcamp_ros2_ws/src
RUN mkdir -p ~/test_ros2_ws/src
RUN cd ~/test_ros2_ws/src




