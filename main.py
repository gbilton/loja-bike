from fastapi import FastAPI, Depends
from database import engine, get_db, SessionLocal
import models
import schemas

app = FastAPI()

models.Base.metadata.create_all(engine)

@app.get('/')
def home():
    return {'mensagem': 'Bem vindo a loja de bikes!'}

@app.get('/api/products')
def item(db: SessionLocal = Depends(get_db)):
    result = db.query(models.Produto).all()
    return result

@app.get('/api/costumers')
def item(db: SessionLocal = Depends(get_db)):
    result = db.query(models.Cliente).all()
    return result

@app.get('/sales')
def item(db: SessionLocal = Depends(get_db)):
    result = db.query(models.Venda).all()
    return result

@app.get('/api/products/{id}')
def item(id: int, db: SessionLocal = Depends(get_db)):
    result = db.query(models.Produto).all()[id]
    return result

@app.get('/api/costumers/{id}')
def item(id: int, db: SessionLocal = Depends(get_db)):
    result = db.query(models.Cliente).all()[id]
    return result

@app.get('/sales/{id}')
def item(id: int, db: SessionLocal = Depends(get_db)):
    result = db.query(models.Venda).all()[id]
    return result


@app.post('/api/products')
def nova_bike(bike: schemas.Bicicleta, db: SessionLocal = Depends(get_db)):
    new_bike = models.Produto(marca=bike.marca, modelo=bike.modelo,
                        ano=bike.ano, cor=bike.cor, preco=bike.preco)
    db.add(new_bike)
    db.commit()

@app.post('/api/costumers')
def novo_cliente(cliente: schemas.Cliente, db: SessionLocal = Depends(get_db)):
    new_costumer = models.Cliente(nome=cliente.nome, idade=cliente.idade)
    db.add(new_costumer)
    db.commit()

@app.post('/api/sales')
def nova_venda(venda: schemas.Venda, db: SessionLocal = Depends(get_db)):
    new_sale = models.Venda(id_cliente=venda.id_cliente,
                            id_produto=venda.id_produto,
                            id_venda=venda.id_venda)
    db.add(new_sale)
    db.commit()
