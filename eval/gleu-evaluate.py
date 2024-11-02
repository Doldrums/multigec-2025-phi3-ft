import os
import sys
from gleu.corpus_main import corpus_main

from utils_transform_markdown_to_one_essay_per_line import get_corpus_names

MODE = sys.argv[1]
HYPO = 1 if MODE == "minimal" else 2

corpuses = get_corpus_names("ref")

for corpus in corpuses:
    print(f"Evaluating for corpus {corpus}:")

    corpus_main({
        "source_path": os.path.join("ref", f"{corpus}-orig-dev.m2"),
        "ref_path_list": [os.path.join("res", f"{corpus}-hypo{HYPO}-dev.m2")],
        "hyp_path_list": ["AMU", "CAMB", "INPUT", "REF0"],
        "digit": 4,
        "fix_seed": True
    })
