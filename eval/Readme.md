# Based on MultiGEC-2025 local evaluation

## Data Preparation:

Firstly download markdown files from https://github.com/spraakbanken/multigec-2025-participants/tree/main/local_eval/errant/ref and place them in ref folder like this:

```txt
eval
`-- ref
    |-- en-writeandimprove2024-orig-dev.md
    `-- it-merlin-orig-dev.md
```

## Model inference:

Run `python3.11 infer.py <minimal|fluency>` to predict fixes for all corpuses.

## GLEU Score:

Python `gleu` package expects linewise-parallel files, so run `python3.11 transform-data.py` to convert both original and solution files.

Instructions for installing `gleu` can be found [here](https://github.com/shotakoyama/gleu?tab=readme-ov-file#usage)

After installation run `python3.11 gleu-evaluate.py <minimal|fluency>`. Scores for each corpus will be output in terminal for.
