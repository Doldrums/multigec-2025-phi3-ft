import os
import sys
from tqdm import tqdm
from mlx_lm.utils import *

from utils_transform_markdown_to_one_essay_per_line import get_corpus_names, md_to_dict


MODE = sys.argv[1]
MODEL = f"../models/phi3-gec-{MODE}"

if MODE == "minimal":
    task_prompt = "Make the smallest possible change in order to make the essay grammatically correct. Change as few words as possible. Do not rephrase parts of the essay that are already grammatical. Do not change the meaning of the essay by adding or removing information. Pay attention to the plurals, articles, compound words. If the essay is already grammatically correct, you should output the original essay without changing anything."
else:
    task_prompt = "You may rephrase parts of the essay to improve fluency. Do not change the meaning of the essay by adding or removing information. Pay attention to the plurals, articles, compound words. If the essay is already grammatically correct and fluent, you should output the original essay without changing anything."


model, tokenizer = load(
    path_or_hf_repo=MODEL,
)


def dict_to_md(essay_dict):
    md = ""
    for essay_id, essay_text in essay_dict.items():
        md += "### essay_id = {}\n{}\n\n".format(essay_id, essay_text)
    return md


def run_model(essay):
    response = generate(
        model, tokenizer, prompt=f"<|system|>{task_prompt}<|end|><|user|>{essay}<|end|>",
        temp=0.1, max_tokens=2048,
    )
    return response.replace("<|assistant|>", "").replace("<|end|>", "").strip()


corpuses = get_corpus_names("ref")
for corpus_name in corpuses:
    with open(os.path.join("ref", f"{corpus_name}-orig-dev.md")) as md:
        corpus = md_to_dict(md.read())

    infer_corpus = dict_to_md(
        {
            essay_id: run_model(essay) for essay_id, essay in tqdm(corpus.items())
        }
    )

    hypo = 1 if MODE == "minimal" else 2
    with open(os.path.join("res", f"{corpus_name}-hypo{hypo}-dev.md"), "w") as md:
        md.write(infer_corpus)
