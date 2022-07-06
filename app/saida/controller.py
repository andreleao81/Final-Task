from app.saida.model import Saida
from flask import request, jsonify
from flask.views import MethodView

class SaidaCreate(MethodView):
    
    def post(self):

        body = request.json

        produto = body.get("produto")
        codigo = body.get("codigo")
        #validade = body.get("validade")
        responsavel = body.get("responsavel")

        if isinstance(produto, str) and\
            isinstance(codigo, str) and\
                isinstance(responsavel, int):

            saida = Saida.query.filter(codigo=codigo).first()
                                


        return None