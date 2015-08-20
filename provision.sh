#!/bin/bash

apt-get update
apt-get install -y python-pip python2.7-dev libzmq-dev
pip install "ipython[notebook]==3.2.1"
pip install emoji
