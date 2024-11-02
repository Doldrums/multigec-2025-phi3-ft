import os
import pandas as pd

# More languages can be added from https://github.com/spraakbanken/multigec-2025-participants/
LANGUAGES = ["english", "italian"]
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
    splits = {split: {"orig": [], "ref1": []} for split in SPLITS}

    files = os.listdir(folder)

    for split in SPLITS:
        parts = [
            file_path for file_path in files if file_path.endswith(f"{split}.md")
        ]
        base_name = "-".join(parts[0].split("-")[0:-2])

        orig_name = os.path.join(folder, f"{base_name}-orig-{split}.md")
        ref1_name = os.path.join(folder, f"{base_name}-ref1-{split}.md")

        orig, ref1 = md_to_dict(orig_name), md_to_dict(ref1_name)

        for key in orig.keys():
            splits[split]["orig"].append(orig[key])
            splits[split]["ref1"].append(ref1[key])

    for split in SPLITS:
        splits[split] = pd.DataFrame.from_dict(splits[split])

    return splits
