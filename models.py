from pydantic import BaseModel, Field

class Filmes(BaseModel):
    titulo: str
    diretor: str
    genero: str
    ano: int = Field(..., ge=1850, le=2100)
    avaliação: int = Field(..., ge=0, le=10)