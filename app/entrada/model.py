from flask import Blueprint
from app.extensions import db
from app.model import BaseModel


entrada_api = Blueprint("entrada_api", __name__)

class Entrada(BaseModel):
    """Estrutura a tabela relacionada \
        aos produtos que foram cadastrados no estoque"""

    __tablename__ = 'entrada'


    produto = db.Column(db.String()) 
    codigo = db.Column(db.String(11), unique = True) 
    validade = db.Column(db.String())
    responsavel = db.Column(db.Integer, db.ForeignKey("funcionario.id"))


def json(self):
        
        return {
            "id": self.id,
            "produto": self.produto,
            "codigo": self.codigo,
            "validade": self.validade,
            "responsavel": self.responsavel
        }
