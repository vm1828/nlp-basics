import os
import re
from shared.constants import *


def load_corpus(dir_path: str) -> list[list[str]]:
    """
    Load a text corpus from .txt files, splitting each file into chapters.

    Returns:
        List[List[str]]: Each inner list contains chapter texts from one file.
    """
    corpus = []
    files = sorted([os.path.join(dir_path, f) for f in os.listdir(dir_path)])
    for file in files:
        with open(file, 'r') as f:
            text = f.read().strip()
            text = re.sub(r'\n+', ' ', text)
            split_text = re.split(PATTERN_CHAPTER_LINE, text)
            corpus.append(split_text)
    return corpus
