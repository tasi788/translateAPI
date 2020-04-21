from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pydantic import BaseModel

from translate import Translate

app = FastAPI()


class Querys(BaseModel):
    InputText: str


@app.get('/ping')
def ping():
    return {'status': True, 'result': 'pong'}


@app.get('/', response_class=HTMLResponse)
def home():
    return open('./webpage/index.html', 'r').read()


@app.get('/script.js', response_class=HTMLResponse)
def jsfile():
    return open('./webpage/script.js', 'r').read()


@app.post('/')
def translation(query: Querys):
    transite = ['google', 'bing']
    ts = Translate()
    for site in transite:
        getattr(ts, site)(query.InputText)
    return ts.result_list
