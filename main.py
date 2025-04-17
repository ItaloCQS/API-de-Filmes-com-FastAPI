from fastapi import FastAPI, HTTPException
from typing import List
from models import Filmes

app = FastAPI()
filmes_db: List[Filmes] = []

@app.get("/")
def home():
    return ("API funcionando")

@app.get("/filmes", response_model = List[Filmes])
def listar_filmes():
    return filmes_db

@app.post("/filmes", response_model = Filmes)
def adicionar_filmes(filmes: Filmes):
    filmes_db.append(filmes)
    return filmes

@app.get("/filmes/{id}", response_model = Filmes)
def obter_filme(id: int):
    if id < 0 or id >= len(filmes_db):
        raise HTTPException(status_code=404, detail="Filme não encontrado")
    return filmes_db[id]

@app.put("/filmes/{id}", response_model = Filmes)
def atualizar_filme(id: int, filme: Filmes):
    if id < 0 or id >= len(filmes_db):
        raise HTTPException(status_code=404, detail="Filme não encontrado") 
    else:
        filmes_db[id] = filme
        return filme
    
@app.delete("/filmes/{id}")
def deletar_filme(id: int):
    if id < 0 or id >= len(filmes_db):
        raise HTTPException(status_code=404, detail="Filme não encontrado") 
    else:
        filmes_db.pop(id)
        return {"mensagem": "Filme removido com sucesso"}