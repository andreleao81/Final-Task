from app.funcionario.model import Funcionario
from flask import request, jsonify
from flask.views import MethodView

class FuncionarioCreate(MethodView):
    
    def post(self):

        body = request.json

        nome = body.get("nome")
        cpf = body.get("cpf")
        senha = body.get("senha")
        turno = body.get("turno")

        return None




    
