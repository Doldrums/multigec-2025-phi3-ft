import os
import sys
import pandas as pd
from tabulate import tabulate

from utils import LANGUAGES, SPLITS, load_folder

# MLX uses different naming for splits
SPLIT_MAP = {"dev": "valid", "train": "train"}
DATA_PATH = "data"

MODE = sys.argv[1]
ENABLE_SYSTEM_PROMPT = sys.argv[2] == "true" if len(sys.argv) > 2 else False

if MODE == "minimal":
    task_prompt = "Make the smallest possible change in order to make the essay grammatically correct. Change as few words as possible. Do not rephrase parts of the essay that are already grammatical. Do not change the meaning of the essay by adding or removing information. Pay attention to the plurals, articles, compound words. If the essay is already grammatically correct, you should output the original essay without changing anything."
else:
    task_prompt = "You may rephrase parts of the essay to improve fluency. Do not change the meaning of the essay by adding or removing information. Pay attention to the plurals, articles, compound words. If the essay is already grammatically correct and fluent, you should output the original essay without changing anything."


def text_format(row):
    if MODE == "minimal":
        ref = row.ref1
    else:
        ref = row.ref2

    system_prompt = f"<|system|>{task_prompt}<|end|>" if ENABLE_SYSTEM_PROMPT else ""

    return f"{system_prompt}<|user|>{row.orig}<|end|><|assistant|>{ref}<|end|>"


merged_data = []
for language in LANGUAGES:
    lang_corpus = load_folder(os.path.join("languages", language))
    merged_data.append(lang_corpus)


merged_data = pd.concat(merged_data)
merged_data["text"] = merged_data.apply(text_format, axis=1)

def print_statistics():
    print("Essays count by corpus:\n")

    table = []
    for corpus in set(merged_data["corpus"]):
        row = [corpus]
        for split in SPLITS:
            count = len(merged_data.loc[(merged_data["corpus"] == corpus) & (merged_data["split"] == split)])
            row.append(count)
        table.append(row)

    print(tabulate(table, headers=["Corpus", *SPLITS]))
    print()

    print("Essays count by language:\n")

    table = []
    for language in set(merged_data["lang"]):
        row = [language]
        for split in SPLITS:
            count = len(merged_data.loc[(merged_data["lang"] == language) & (merged_data["split"] == split)])
            row.append(count)
        table.append(row)

    print(tabulate(table, headers=["Language", *SPLITS]))
    print()

print("Before balancing:\n")

print_statistics()

balanced_data = []

for split in SPLITS:
    split_group = merged_data.loc[merged_data["split"] == split].groupby("lang")
    target_size = split_group.size().min() + int((split_group.size().max() - split_group.size().min()) * 0.5)

    df =  split_group[merged_data.columns].apply(lambda x: x.sample(target_size, replace=len(x) < target_size), include_groups=False).reset_index(drop=True)
    balanced_data.append(df)

merged_data = pd.concat(balanced_data).sample(frac=1)

print("After balancing:\n")

print_statistics()

# merge all languages in one dataset and save in MLX jsonl format
for split in SPLITS:
    merged_data.loc[merged_data["split"] == split][["text"]].to_json(
        os.path.join(DATA_PATH, f"{SPLIT_MAP[split]}.jsonl"),
        force_ascii=False,
        orient="records",
        lines=True
    )
