
from app.extensions import db
from app.model import BaseModel
from flask import Blueprint


cliente_api = Blueprint("cliente_api", __name__)

class Cliente(BaseModel):
    
    __tablename__ = 'cliente'

    nome = db.Column(db.String(128)) 
    cnpj = db.Column(db.String(11), unique = True) 
    senha = db.Column(db.String(100))
    endereco = db.Column(db.String(100))
    entregas = db.relationship("saída", backref="cliente")
  