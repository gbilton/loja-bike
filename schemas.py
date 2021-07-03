from pydantic import BaseModel


class Bicicleta(BaseModel):
    marca: str
    modelo: str
    ano: int
    cor: str
    preco: float

class Cliente(BaseModel):
    nome: str
    idade: int
    n_compras: int

class Venda(BaseModel):
    cliente: int
    produto: int
    quantidade: int
    valor: float
    
