import os
import pandas as pd

# More languages can be added from https://github.com/spraakbanken/multigec-2025-participants/
LANGUAGES = [file for file in os.listdir("languages") if file != ".gitignore"]
SPLITS = ["dev", "train"]


def md_to_dict(md_path):
    # Reads md format
    with open(md_path) as md_file:
        md = md_file.read()
        essay_dict = {}

        for essay in md.split("### essay_id = ")[1:]:
            (essay_id, text) = essay.split("\n", maxsplit=1)
            essay_dict[essay_id] = text.strip("\n")
        return essay_dict


def load_folder(folder):
    rows = []

    files = os.listdir(folder)

    for split in SPLITS:
        datasets = set(
            "-".join(file_path.split("-")[0:-2]) for file_path in files if file_path.endswith(f"{split}.md")
        )

        for dataset in datasets:
            dataset_lang = dataset.split("-")[0]

            orig_name = os.path.join(folder, f"{dataset}-orig-{split}.md")
            ref1_name = os.path.join(folder, f"{dataset}-ref1-{split}.md")
            ref2_name = os.path.join(folder, f"{dataset}-ref2-{split}.md")

            orig = md_to_dict(orig_name)
            ref1 = md_to_dict(ref1_name)
            ref2 = None

            if os.path.exists(ref2_name):
                ref2 = md_to_dict(ref2_name)

            for key in orig.keys():
                row = {
                    "corpus": dataset,
                    "lang": dataset_lang,
                    "orig": orig[key],
                    "ref1": ref1[key],
                    "split": split
                }

                if ref2 is not None and key in ref2:
                    row["ref2"] = ref2[key]
                else:
                    row["ref2"] = ref1[key]

                rows.append(row)

    return pd.DataFrame.from_dict(rows)
