#!/bin/bash

for i in `seq 1 120`;do
raspistill -o ./laser_image.jpg
python3 laseranalysis.py
sleep 30s
done
