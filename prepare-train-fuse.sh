#!/bin/bash
python3.11 prepare-data.py $1
./mlx-train.sh
./mlx-fuse.sh $1
