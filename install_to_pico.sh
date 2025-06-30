#!/bin/bash

source .venv/bin/activate

rshell -p /dev/ttyACM0 --buffer-size 512 cp main.py /pyboard/main.py

