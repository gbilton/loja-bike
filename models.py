import datetime
from sqlalchemy import Column, Integer, String, Float, DateTime
from database import Base


class Produto(Base):
    __tablename__ = 'produtos'

    id = Column(Integer, primary_key=True, autoincrement=True)
    marca = Column(String)
    modelo = Column(String)
    ano = Column(Integer)
    cor = Column(String)
    preco = Column(Float)


class Cliente(Base):
    __tablename__ = 'clientes'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String, unique=True)
    idade = Column(Integer)
    n_compras = Column(Integer, default=0)


class Venda(Base):
    __tablename__ = 'vendas'

    id = Column(Integer, primary_key=True, autoincrement=True)
    cliente = Column(Integer)
    produto = Column(Integer)
    quantidade = Column(Integer)
    valor = Column(Float)
    data = Column(DateTime, default=datetime.datetime.now())
