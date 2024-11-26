# Solution for: Shared task on Multilingual Grammatical Error Correction (MultiGEC-2025)

#### Author: Arina Kharlamova (Arina.Kharlamova@mbzuai.ac.ae)

## Data Preparation:

Firstly download all available datasets from https://github.com/spraakbanken/multigec-2025-participants/ and place in separate folders. See Readme.md in `languages/english` and `languages/italian` folder as example.

Then run `python3.11 prepare-data.py <minimal|fluency> <true|false>`, this will convert and merge all datasets in single MLX dataset.

First parameter controls level of edits (See more in [task description](https://github.com/spraakbanken/multigec-2025?tab=readme-ov-file#task-description))
Second parameter disables/enables injecting of system prompt to datasets

## Model Preparation:

Run `python3.11 mlx-convert.py`, and wait for while. It will download Microsoft Phi3-Mini-128k model.

## Training:

Run `./mlx-train.sh` for training adapter. LORA configuration can be found in `lora-config.yaml`

```yaml
lora_parameters:
  keys: ["self_attn.o_proj", "self_attn.qkv_proj"] # keys recommened by Phi-3 finetune cookbook.
```

After training, model can be merged with adapters in single compiled model by running `./mlx-fuse.sh <minimal|fluency>`

## Evaluation:

Follow instructions from [eval/Readme.md](eval/Readme.md) to evaluate model.
