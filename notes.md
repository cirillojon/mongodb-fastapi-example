# Notes

## Create virtualenv:
python -m virtualenv venv 

## Activate virtualenv:
venv/scripts/activate

## Install dependencies:
pip install pymongo fastapi uvicorn

## Run server:
uvicorn index:app --reload

## Connect to mongodb with:
mongodb://localhost:27017/

## Swagger page automatically created at:
http://127.0.0.1:8000/docs