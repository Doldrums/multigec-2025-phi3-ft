# Based on MultiGEC-2025 local evaluation

## Data Preparation:

Firstly download markdown files from https://github.com/spraakbanken/multigec-2025-participants/tree/main/local_eval/errant/ref and place them in `ref` folder like this:

```txt
ref
|-- en-writeandimprove2024-orig-dev.md
|-- en-writeandimprove2024-ref1-dev.md
|-- it-merlin-orig-dev.md
`-- it-merlin-ref1-dev.md
```

## Model inference:

Run `python3.11 infer.py <minimal|fluency> <true|false>` to predict fixes for all corpuses.

First parameter controls level of edits (See more in [task description](https://github.com/spraakbanken/multigec-2025?tab=readme-ov-file#task-description))
Second parameter disables/enables injecting of system prompt when generating

## GLEU Score:

Python `gleu` package expects linewise-parallel files, so run `python3.11 transform-data.py` to convert both original and solution files.

Instructions for installing `gleu` can be found [here](https://github.com/shotakoyama/gleu?tab=readme-ov-file#usage)

After installation run `python3.11 gleu-evaluate.py <minimal|fluency>`. Scores for each corpus will be output in terminal:

```bash
Evaluating for corpus it-merlin:
ref/it-merlin-orig-dev.m2       33.4006 # unfixed text
res/it-merlin-hypo1-dev.m2      51.8245 # this solutions
ref/it-merlin-ref-1.m2  100.0000 # human solution

Evaluating for corpus en-writeandimprove2024:
ref/en-writeandimprove2024-orig-dev.m2  57.6481
res/en-writeandimprove2024-hypo1-dev.m2 69.4036
ref/en-writeandimprove2024-ref-1.m2     100.0000
```
