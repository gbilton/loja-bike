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

class Venda(BaseModel):
    id_venda: int
    id_cliente: int
    id_produto: int
