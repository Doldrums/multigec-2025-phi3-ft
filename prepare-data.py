import os
import sys
import pandas as pd

from utils import LANGUAGES, SPLITS, load_folder

# MLX uses different naming for splits
SPLIT_MAP = {"dev": "valid", "train": "train"}
DATA_PATH = "data"

MODE = sys.argv[1]

if MODE == "minimal":
    task_prompt = "Make the smallest possible change in order to make the essay grammatically correct. Change as few words as possible. Do not rephrase parts of the essay that are already grammatical. Do not change the meaning of the essay by adding or removing information. Pay attention to the plurals, articles, compound words. If the essay is already grammatically correct, you should output the original essay without changing anything."
else:
    task_prompt = "You may rephrase parts of the essay to improve fluency. Do not change the meaning of the essay by adding or removing information. Pay attention to the plurals, articles, compound words. If the essay is already grammatically correct and fluent, you should output the original essay without changing anything."


def text_format(row):
    if MODE == "minimal":
        ref = row.ref1
    else:
        ref = row.ref2

    return f"<|system|>{task_prompt}<|end|><|user|>{row.orig}<|end|><|assistant|>{ref}<|end|>"


merged_data = {split: [] for split in SPLITS}
for language in LANGUAGES:
    lang_corpus = load_folder(os.path.join("languages", language))

    for split in SPLITS:
        merged_data[split].append(lang_corpus[split])

for split in SPLITS:
    merged_data[split] = pd.concat(merged_data[split])
    merged_data[split]["text"] = merged_data[split].apply(text_format, axis=1)

# merge all languages in one dataset and save in MLX jsonl format
for split in SPLITS:
    merged_data[split][["text"]].to_json(
        os.path.join(DATA_PATH, f"{SPLIT_MAP[split]}.jsonl"),
        force_ascii=False,
        orient="records",
        lines=True
    )
