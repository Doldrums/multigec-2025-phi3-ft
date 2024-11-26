#!/bin/bash
echo "Preparing data..."
time python3.11 prepare-data.py $1 $2
echo "Training model..."
time ./mlx-train.sh
echo "Fusing model for inference..."
time ./mlx-fuse.sh $1
echo "Done!"
