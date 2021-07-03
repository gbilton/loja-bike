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


class Venda(Base):
    __tablename__ = 'vendas'

    id = Column(Integer, primary_key=True, autoincrement=True)
    id_cliente = Column(Integer)
    id_produto = Column(Integer)
    quantidade = Column(Integer)
    data = Column(DateTime, default=datetime.datetime.now())
