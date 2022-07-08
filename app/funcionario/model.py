from app.extensions import db
from app.model import BaseModel
from flask import Blueprint

funcionario_api = Blueprint("funcionario_api", __name__)

class Funcionario(BaseModel):
    __tablename__ = 'funcionario'

    nome = db.Column(db.String()) 
    cpf = db.Column(db.String(11), unique = True) 
    senha = db.Column(db.String(), unique = True, nullable = False)
    email = db.Column(db.String(100), unique = True, nullable = False)
    turno = db.Column(db.Integer())

    entradas = db.relationship("entrada", backref = "funcionario")
    saidas = db.relationship("saída", backref = "funcionario")
    
    def json(self):
        
        return {
            "id": self.id,
            "nome": self.nome,
            "cpf": self.cpf,
            "email": self.email,
            "turno": self.turno
        }
