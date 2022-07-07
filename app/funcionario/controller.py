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
        









    
