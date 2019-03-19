#!/bin/bash
for i in `seq 1 10`;
do
raspstill -o ./laser_image.jpg
python3 laseranalysis.py
sleep 60s
done
