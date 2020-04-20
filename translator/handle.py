from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
class Querys(BaseModel):
    InputText: str

@app.get('/ping')
def ping():
    return {'status': True, 'result': 'pong'}


@app.post('/')
def translation(query: Querys):
    pass