import re

from shared.constants import PUNCTUATION


def remove_punctuation(text: str) -> str:
    text = text.translate(
        str.maketrans("", "", PUNCTUATION))
    text = re.sub(r'-{2,}', ' ', text)  # remove hyphens if more than 1
    return text
