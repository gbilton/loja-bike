from fastapi import FastAPI, Depends
from database import engine, get_db, SessionLocal
import models
import schemas

app = FastAPI()

models.Base.metadata.create_all(engine)

@app.get('/')
def home():
    return {'test': 'successful'}

@app.post('/addbike')
def nova_bike(bike: schemas.Bicicleta, db: SessionLocal = Depends(get_db)):
    new_bike = models.Produto(marca=bike.marca, modelo=bike.modelo,
                        ano=bike.ano, cor=bike.cor, preco=bike.preco)
    db.add(new_bike)
    db.commit()
