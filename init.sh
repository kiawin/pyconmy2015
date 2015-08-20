#!/usr/bin/env bash

# Update packages and install python-pip
yaourt -Syy
yaourt -S --noconfirm python-pip

# Setup python virtual environment
rm -rf /vagrant/venv/pycon
mkdir -p /vagrant/venv
pyvenv /vagrant/venv/pycon

# Enable virtual environment for all ssh session
echo "source /vagrant/venv/pycon/bin/activate\ncd /vagrant" >> ~/.bashrc
echo "source /vagrant/venv/pycon/bin/activate\ncd /vagrant" >> /home/vagrant/.bashrc

# Install python modules to python virtual environment
source /vagrant/venv/pycon/bin/activate
pip install --upgrade pip
pip install PyYAML
