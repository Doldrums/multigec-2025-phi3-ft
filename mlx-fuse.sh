#!/bin/bash
python3.11 -m mlx_lm.fuse \
    --model mlx-model \
    --adapter-path adapters \
    --save-path models/phi3-gec-$1 \
    --de-quantize
