from app.cliente.model import Cliente
from flask import request, jsonify
from flask.views import MethodView
import bcrypt
from flask_jwt_extended import create_access_token
from app.extensions import db, mail

class ClienteCreate(MethodView):
    
    def post(self):

        body = request.json
        a = db.Query

        nome = body.get("nome")
        cnpj = body.get("cnpj")
        endereco = body.get("endereco")
        senha = body.get("senha")
        senha = bcrypt.hashpw(senha.encode(), bcrypt.gensalt().decode())

        if isinstance(nome, str) and\
            isinstance(cnpj, str) and\
                isinstance(endereco, str) and\
                    isinstance(senha, str):

            cliente = Cliente.query.filter_by(cnpj=cnpj).first()

            if cliente:
                return   {"code status":"Dados inválidos, cliente já cadastrado"}, 400
            
            cliente = Cliente(nome = nome,\
                                cnpj = cnpj, \
                                    senha = senha,\
                                        endereco = endereco)

            cliente.save()

        return cliente.json(), 200


    def get(self):

        clientes = Cliente.query.all()

        return jsonify([cliente.json() for cliente in clientes]), 200

    
class ClienteDetails(MethodView):

    def get(self, id):
        
        cliente = Cliente.query.get_or_404(id)

        return cliente.json()
    
    def put(self, id):

        body = request.json()
        
        nome = body.get("nome")
        cnpj = body.get("cnpj")
        endereco = body.get("endereco")
        senha = body.get("senha")

        if isinstance(nome, str) and\
            isinstance(cnpj, str) and\
                isinstance(endereco, str)and\
                    isinstance(senha, str):

            cliente = Cliente.query.filter_by(cnpj=cnpj).first()

            if cliente:
                return   ("code status: Dados inválidos, Cliente já cadastrado"), 400
            
            cliente.nome = nome
            cliente.cnpj = cnpj
            cliente.endereco = endereco
            cliente.senha = senha


            cliente.update()

            return cliente.json(), 200

        else:
            return {"code status":"Dados invalidos"}, 400

    
    def patch(self, id):

        body = request.json()
        cliente = Cliente.query.get_or_404(id)
        
        nome = body.get("nome", cliente.nome)
        cnpj = body.get("cnpj", cliente.nome)
        endereco = body.get("endereco", cliente.endereco)
        senha = body.get("senha", cliente.senha)

        if isinstance(nome, str) and\
            isinstance(cnpj, str) and\
                isinstance(endereco, str)and\
                    isinstance(senha, str):

            cliente = Cliente.query.filter_by(cnpj=cnpj).first()

            if cliente:
                return   ("code status: Dados inválidos, Cliente já cadastrado"), 400
            
            cliente.nome = nome
            cliente.cnpj = cnpj
            cliente.endereco = endereco
            cliente.senha = senha

            cliente.update()

            return cliente.json(), 200

        else:
            return {"code status":"Dados invalidos"}, 400
    
    def delete(self, id):

        cliente = Cliente.query.get_or_404(id)
        cliente.delete(cliente)

        return cliente.json()
        

class Login(MethodView):
    
    def post(self):

        dados = request.json()

        email = dados.get("email")
        senha = dados.get("senha")

        cliente = Cliente.query.filter_by(email = email, senha = senha)
        
        if cliente and bcrypt.checkpw(senha.encode(), cliente.senha.encode()):
            return 200, {"token": create_access_token(cliente.id, additional_claims={"cliente":"logado"})}
        return {"msg":"usuario ou email invalidos"}, 400
        


