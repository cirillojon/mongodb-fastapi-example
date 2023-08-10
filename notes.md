# Notes

## Create virtualenv:
python -m virtualenv venv 

## Activate virtualenv:
venv/scripts/activate

## Install dependencies:
pip install pymongo fastapi uvicorn

## Run server:
uvicorn index:app --reload