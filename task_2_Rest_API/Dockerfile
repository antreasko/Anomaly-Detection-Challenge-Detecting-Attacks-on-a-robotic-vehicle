FROM ubuntu:18.04

# Set some variables
# ENV USER antreas
# ENV HOME /home/$USER
# ENV DIR flask_app

RUN apt-get update && apt-get upgrade -y
RUN apt-get -y install locales sudo build-essential cmake git

# Install libraries
RUN apt-get update && apt-get install -y \
    python3-venv

# Add user and change to user

# RUN useradd -m $USER -G sudo && \
#     echo "$USER:$USER" | chpasswd && \
#     echo "$USER ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers
# USER $USER
# # Create shared volume
# VOLUME $HOME/$DIR
# WORKDIR $HOME/$DIR

# # Start bash login shell
# ENTRYPOINT ["/bin/bash", "-l", "-c"]
# CMD ["/bin/bash", "-i"]
