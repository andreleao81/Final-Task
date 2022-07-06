from app.entrada.model import Entrada
from flask import request, jsonify
from flask.views import MethodView

class EntradaCreate(MethodView):
    
    def post(self):

        body = request.json

        produto = body.get("produto")
        codigo = body.get("codigo")
        #validade = body.get("validade")
        responsavel = body.get("responsavel")

        if isinstance(produto, str) and\
            isinstance(codigo, str) and\
                isinstance(responsavel, int):

            entrada = Entrada.query.filter(codigo=codigo).first()
                                


        return None
