import os
import sys
from unicodedata import category


TXT_PNP = os.path.join('data', 'pnp', 'pnp.txt')
JSON_CHARACTERS_PNP = os.path.join('data', 'pnp_characters.json')
JSON_CHARACTERS_HP = os.path.join('data', 'hp_characters.json')
DIR_PNP = os.path.join('data', 'pnp')
DIR_HP = os.path.join('data', 'hp')

# utf-8 punctuation
PUNCTUATION = ''.join([chr(i) for i in range(sys.maxunicode)
                       if category(chr(i)).startswith("P") and chr(i) != '-'])

PATTERN_CHAPTER_LINE = r"(?i)\s*CHAPTER\s*\d{1,2}\s*"
