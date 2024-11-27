import os
import sys
from tqdm import tqdm
from mlx_lm.utils import *

from utils import LANGUAGE_CODES
from utils_transform_markdown_to_one_essay_per_line import get_corpus_names, md_to_dict


MODE = sys.argv[1]
ENABLE_SYSTEM_PROMPT = sys.argv[2] == "true" if len(sys.argv) > 2 else False
LANGUAGE_FILTER = sys.argv[3].split(",") if len(
    sys.argv) > 3 else LANGUAGE_CODES

MODEL = f"../models/phi3-gec-{MODE}"

if MODE == "minimal":
    task_prompt = "Make minimal changes to correct grammar while preserving meaning. Leave already correct parts unchanged."
else:
    task_prompt = "Rephrase to improve fluency, keeping the meaning unchanged. Leave already correct and fluent text as is."


model, tokenizer = load(
    path_or_hf_repo=MODEL,
)


def dict_to_md(essay_dict):
    md = ""
    for essay_id, essay_text in essay_dict.items():
        md += "### essay_id = {}\n{}\n\n".format(essay_id, essay_text)
    return md


def run_model(essay):
    system_prompt = f"<|system|>{task_prompt}<|end|>" if ENABLE_SYSTEM_PROMPT else ""

    response = generate(
        model, tokenizer, prompt=f"{system_prompt}<|user|>{essay}<|end|>",
        temp=0.1, max_tokens=9216,
    )
    return response.replace("<|assistant|>", "").replace("<|end|>", "").strip()


corpuses = get_corpus_names("ref")
for corpus_name in corpuses:
    corpus_lang = corpus_name.split("-")[0]
    if corpus_lang not in LANGUAGE_FILTER:
        continue

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
