from app.extensions import db
from app.model import BaseModel
from flask import Blueprint

saida_api = Blueprint("saida_api", __name__)

class Saida(BaseModel):
    """Estrutura a tabela relacionada \
        aos produtos que foram cadastrados no estoque,
        mas foram removidos"""

    __tablename__ = 'saída'

    produto = db.Column(db.String()) # string limitada
    codigo = db.Column(db.String(11)) 
    validade = db.Column(db.String(50))
    responsavel = db.Column(db.Integer, db.ForeignKey("funcionario.id"))
    cliente = db.Column(db.Integer, db.ForeignKey("cliente.id"))

    