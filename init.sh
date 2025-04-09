#!/bin/bash

echo "" && echo "===================================================== PROJECT INIT" && echo ""

if [ ! -d ".venv" ]; then
    python3 -m venv .venv
    source .venv/bin/activate
    pip install wheel
    pip install -r requirements.txt

    python3 -m spacy download en_core_web_sm
    python3 -m spacy download en_core_web_lg
    python3 -m nltk.downloader -d ./.venv/nltk_data punkt_tab
else
    echo "Project already initialized."
fi

echo ""
