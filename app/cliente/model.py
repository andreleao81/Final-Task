
from enum import unique
from app.extensions import db
from app.model import BaseModel
from flask import Blueprint


cliente_api = Blueprint("cliente_api", __name__)

class Cliente(BaseModel):
    
    __tablename__ = 'cliente'

    nome = db.Column(db.String(128)) 
    cnpj = db.Column(db.String(11), unique = True) 
    senha = db.Column(db.String(), unique = True, nullable = False)
    email = db.Column(db.String(100), unique = True, nullable = False)
    endereco = db.Column(db.String(100))
    entregas = db.relationship("saída", backref="cliente")


def json(self):
        
        return {
            "id": self.id,
            "nome": self.nome,
            "cnpj": self.cnpj,
            "email": self.email,
            "endereco": self.endereco
        }
