'''uvicorn test:app --reload'''

from fastapi import FastAPI
import pydantic

app = FastAPI()

@app.get('/')
def home():
    return {'Data': 'Testing'}

@app.get('/checkout')
def checkout():
    pass
