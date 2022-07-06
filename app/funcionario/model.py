from app.extensions import db
from app.model import BaseModel
from flask import Blueprint

funcionario_api = Blueprint("funcionario_api", __name__)

class Funcionario(BaseModel):
    __tablename__ = 'funcionarios'

    nome = db.Column(db.String()) 
    cpf = db.Column(db.String(11), unique = True) 
    senha = db.Column(db.String(50))
    turno = db.Column(db.Integer())

    entradas = db.relationship("Entrada", backref = "funcionario")
    saidas = db.relationship("Saida", backref = "funcionario")
    
    def json(self):
        
        return {
            "id": self.id,
            "nome": self.nome,
            "cpf": self.cpf,
            "senha": self.senha,
            "turno": self.turno
        }
