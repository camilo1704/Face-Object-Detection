#!/bin/bash
git submodule init
git submodule update
conda create --name yolov8
conda activate yolov8
pip install ./ultralytics/requirements.txt
