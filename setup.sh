#!/bin/bash

wget https://apt.devkitpro.org/install-devkitpro-pacman
chmod +x ./install-devkitpro-pacman
sudo ./install-devkitpro-pacman

sudo dkp-pacman -S nds-dev
sudo apt-get install -y desmume

export PATH=$PATH:/usr/games
source /etc/profile.d/devkit-env.sh
