# Solution for: Shared task on Multilingual Grammatical Error Correction (MultiGEC-2025)

#### Author: Arina Kharlamova (Arina.Kharlamova@mbzuai.ac.ae)

## Data Preparation:

Firstly download all available datasets from https://github.com/spraakbanken/multigec-2025-participants/ and place in separate folders. See Readme.md in `english` and `italian` folder as example.

Then run `python3.11 prepare-data.py <minimal|fluency>`, this will convert and merge all datasets in single MLX dataset.

## Model Preparation:

Run `python3.11 mlx-convert.py`, and wait for while. It will download and quantize Microsoft Phi3-Mini-4k model.

## Training:

Run `./mlx-train.sh` for training adapter. LORA configuration can be found in `lora-config.yaml`

```yaml
lora_parameters:
  keys: ["self_attn.o_proj", "self_attn.qkv_proj"] # keys recommened by Phi-3 finetune cookbook.
```

After training, model can be merged with adapters in single compiled model by running `./mlx-fuze.sh <minimal|fluency>`

## Evaluation:

Follow instructions from [eval/Readme.md](eval/Readme.md) to evaluate model.
