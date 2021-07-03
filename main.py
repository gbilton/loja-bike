from fastapi import FastAPI, Depends
from database import engine, get_db, SessionLocal
import models
import schemas

app = FastAPI()

models.Base.metadata.create_all(engine)

@app.get('/')
def home():
    return {'mensagem': 'Bem vindo a loja de bikes!'}

@app.post('/addbike')
def nova_bike(bike: schemas.Bicicleta, db: SessionLocal = Depends(get_db)):
    new_bike = models.Produto(marca=bike.marca, modelo=bike.modelo,
                        ano=bike.ano, cor=bike.cor, preco=bike.preco)
    db.add(new_bike)
    db.commit()

@app.post('/addcostumer')
def novo_cliente(cliente: schemas.Cliente, db: SessionLocal = Depends(get_db)):
    new_costumer = models.Cliente(nome=cliente.nome, idade=cliente.idade)
    db.add(new_costumer)
    db.commit()

@app.post('/checkout')
def nova_venda(venda: schemas.Venda, db: SessionLocal = Depends(get_db)):
    new_sale = models.Venda(id_cliente=venda.id_cliente,
                            id_produto=venda.id_produto,
                            quantidade=venda.quantidade)
    db.add(new_sale)
    db.commit()

@app.get('/products')
def item(db: SessionLocal = Depends(get_db)):
    result = db.query(models.Produto).all()
    return result

@app.get('/clientes')
def item(db: SessionLocal = Depends(get_db)):
    result = db.query(models.Cliente).all()
    return result

@app.get('/vendas')
def item(db: SessionLocal = Depends(get_db)):
    result = db.query(models.Venda).all()
    return result
