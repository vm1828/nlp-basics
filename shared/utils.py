import json
import re
from typing import Any

from shared.constants import PUNCTUATION


def remove_punctuation(text: str) -> str:
    text = text.translate(
        str.maketrans("", "", PUNCTUATION))
    text = re.sub(r'-{2,}', ' ', text)  # remove hyphens if more than 1
    return text


def load_json(file: str) -> Any:
    with open(file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data
