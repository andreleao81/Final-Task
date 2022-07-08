from app.funcionario.model import Funcionario
from flask import request, jsonify
from flask.views import MethodView
from flask_jwt_extended import create_access_token
import bcrypt


class FuncionarioCreate(MethodView):
    
    def post(self):

        body = request.json

        nome = body.get("nome")
        cpf = body.get("cpf")
        senha = body.get("senha")
        senha = bcrypt.hashpw(senha.encode(), bcrypt.gensalt().decode())
        turno = body.get("turno")

        if isinstance(nome, str) and\
            isinstance(cpf, str) and\
                isinstance(senha, str) and\
                    isinstance(turno, str):

            funcionario = Funcionario.query.filter_by(cpf=cpf).first()

            if funcionario:
                return {"code status":"Dados inválidos, funcionário já cadastrado."}, 400

            funcionario = Funcionario(nome=nome,\
                                cpf=cpf,\
                                    senha=senha,\
                                        turno=turno)
            funcionario.save()
        
        return funcionario.json(), 200
    
    def get(self):

        funcionarios = Funcionario.query.all()

        return jsonify([funcionario.json() for funcionario in funcionarios]),200
                                


class FuncionarioDetails(MethodView):

    def get(self, id):
        
        funcionario = Funcionario.query.get_or_404(id)

        return funcionario.json()
    
    def put(self, id):

        body = request.json()
        
        nome = body.get("nome")
        cpf = body.get("cpf")
        turno = body.get("turno")

        if isinstance(nome, str) and\
            isinstance(cpf, str) and\
                isinstance(turno, int):

            funcionario = Funcionario.query.filter_by(cpf=cpf).first()

            if funcionario:
                return   ("code status: Dados inválidos, funcionario já cadastrado"), 400
            
            funcionario.nome = nome
            funcionario.cpf = cpf
            funcionario.turno = turno

            funcionario.update()

            return funcionario.json(), 200

        else:
            return {"code status":"Dados invalidos"}, 400

    
    def patch(self, id):

        body = request.json()
        funcionario = Funcionario.query.get_or_404(id)
        
        nome = body.get("nome", funcionario.nome)
        cpf = body.get("cpf", funcionario.nome)
        turno = body.get("turno", funcionario.turno)

        if isinstance(nome, str) and\
            isinstance(cpf, str) and\
                isinstance(turno, str):

            funcionario = Funcionario.query.filter_by(cpf=cpf).first()

            if funcionario:
                return   ("code status: Dados inválidos, funcionario já cadastrado."), 400
            
            funcionario.nome = nome
            funcionario.cpf = cpf
            funcionario.turno = turno

            funcionario.update()

            return funcionario.json(), 200
    
    def delete(self, id):

        funcionario = Funcionario.query.get_or_404(id)
        funcionario.delete(funcionario)

        return funcionario.json()
        


class FuncionarioLogin(MethodView):
    
    def post(self):

        dados = request.json()

        email = dados.get("email")
        senha = dados.get("senha")

        funcionario = Funcionario.query.filter_by(email = email, senha = senha)
        
        if funcionario and bcrypt.checkpw(senha.encode(), funcionario.senha.encode()):
            return 200, {"token": create_access_token(funcionario.id, additional_claims={"funcionario":"logado"})}
        return {"msg":"usuario ou email invalidos"}, 400
        








    
