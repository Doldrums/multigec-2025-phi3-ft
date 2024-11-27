import os
import sys
from typing import List
from gleu.count import set_tokenization
from gleu.corpus_main import corpus_main

from utils_transform_markdown_to_one_essay_per_line import get_corpus_names

MODE = sys.argv[1]
HYPO = 1 if MODE == "minimal" else 2

corpuses = get_corpus_names("ref")


class Args:
    def __init__(self, source_path: str, ref_path_list: List[str], hyp_path_list: List[str], digit: int, fix_seed: bool, max: bool = False):
        self.source_path = source_path
        self.ref_path_list = ref_path_list
        self.hyp_path_list = hyp_path_list
        self.digit = digit
        self.fix_seed = fix_seed
        self.max = max
        self.token = "word"
        self.n = 4
        self.iter = 500
        self.proc = 1


for corpus in corpuses:
    hypo_path = os.path.join("res", f"{corpus}-hypo{HYPO}-dev.m2")
    if not os.path.exists(hypo_path):
        continue

    print(f"Evaluating for corpus {corpus}:")

    refs = [os.path.join("ref", f)
            for f in os.listdir("ref") if f.startswith(corpus) and f.endswith(".m2") and "ref" in f
            ]

    args = Args(
        source_path=os.path.join("ref", f"{corpus}-orig-dev.m2"),
        ref_path_list=refs,
        hyp_path_list=[
            os.path.join("ref", f"{corpus}-orig-dev.m2"),
            hypo_path,
            *refs,
        ],
        digit=4,
        fix_seed=True,
        max=False
    )

    set_tokenization(args.token)
    corpus_main(args)

    print()
