from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from translate import Translate

app = FastAPI()

origins = [
    "http://127.0.0.1:5500",
    "http://localhost:5500",
    "http://127.0.0.1:8000"
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class Querys(BaseModel):
    InputText: str


@app.get('/ping')
def ping():
    return {'status': True, 'result': 'pong'}


@app.post('/')
def translation(query: Querys):
    transite = ['gooyou', 'deepl']
    ts = Translate()
    for site in transite:
        getattr(ts, site)(query.InputText)

    return ts.result_list
