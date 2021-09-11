@echo off
echo Time to make the updates
python -m pip install -U pip pip-tools setuptools wheel -I
for %%i in (core_requirements, dev_requirements) do (
    pip-compile --upgrade %%i.in && copy %%i.txt src
)
pip-sync core_requirements.txt dev_requirements.txt
echo Done!
@echo on
