import datetime
from sqlalchemy import Table, Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from database import Base


association_table = Table('association', Base.metadata,
    Column('id_vendas', Integer, ForeignKey('vendas.id_venda')),
    Column('id_produto', Integer, ForeignKey('produtos.id'))
)

class Produto(Base):
    __tablename__ = 'produtos'

    id = Column(Integer, primary_key=True, autoincrement=True)
    marca = Column(String)
    modelo = Column(String)
    ano = Column(Integer)
    cor = Column(String)
    preco = Column(Float)
    children = relationship('Venda',
                    secondary=association_table)

class Cliente(Base):
    __tablename__ = 'clientes'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String, unique=True)
    idade = Column(Integer)

class Venda(Base):
    __tablename__ = 'vendas'

    entries = Column(Integer, primary_key=True, autoincrement=True)
    id_venda = Column(Integer)
    id_cliente = Column(Integer, ForeignKey('clientes.id'))
    id_produto = Column(Integer)
    data = Column(DateTime, default=datetime.datetime.now())
