#!/bin/bash

cd /opt/resume_maker || exit
python3.12 -m venv .venv
source .venv/bin/activate
python -m pip install -U pip pip-tools setuptools wheel
for FILE in core_requirements dev_requirements
do
	pip-compile --resolver=backtracking --upgrade $FILE.in
done
pip-sync core_requirements.txt dev_requirements.txt
python -m nltk.downloader punkt
