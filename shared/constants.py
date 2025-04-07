import os

TXT_FILE = os.path.join('data', 'pnp.txt')
JSON_CHARACTERS = os.path.join('data', 'pnp_characters.json')

PUNCTUATION = '.;,-“’”:?—‘!()_'
PATTERN_CHAPTER_LINE = r"(?i)\s*CHAPTER\s*[IVXLCDM]+[\s.]*"
