import os
import shutil
from mlx_lm.utils import *

MODEL_NAME = "microsoft/Phi-3-mini-128k-instruct"
MLX_PATH = "mlx-model"

if os.path.exists(MLX_PATH):
    shutil.rmtree(MLX_PATH)

# Download and quantize Phi-3-mini-128k-instruct
convert(
    hf_path=MODEL_NAME,
    mlx_path=MLX_PATH
)
