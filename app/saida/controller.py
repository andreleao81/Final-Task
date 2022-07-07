from app.saida.model import Saida
from flask import request, jsonify
from flask.views import MethodView

class SaidaCreate(MethodView):
    
    def post(self):

        body = request.json

        #id = body.get("id")
        produto = body.get("produto")
        codigo = body.get("codigo")
        #validade = body.get("validade")
        responsavel = body.get("responsavel")

        if isinstance(produto, str) and\
            isinstance(codigo, str) and\
                isinstance(responsavel, int):

            saida = Saida.query.filter_by(codigo=codigo).first()

            if saida:
                return   {"code status":"Dados inválidos, saida já realizada"}, 400
            
            saida = Saida(produto = produto,\
                            codigo = codigo, \
                                responsavel = responsavel)

            saida.save()

        return saida.json(), 200


    def get(self):

        saidas = Saida.query.all()

        return jsonify([saida.json() for saida in saidas]), 200
    

class SaidaDetails(MethodView):

    def get(self, id):
        
        saida = Saida.query.get_or_404(id)

        return saida.json()
    
    def put(self, id):

        body = request.json()
        
        produto = body.get("produto")
        codigo = body.get("codigo")
        #validade = body.get("validade")
        responsavel = body.get("responsavel")

        if isinstance(produto, str) and\
            isinstance(codigo, str) and\
                isinstance(responsavel, int):

            saida = Saida.query.filter_by(codigo=codigo).first()

            if saida:
                return   ("code status: Dados inválidos, saida já realizada"), 400
            
            saida.produto = produto
            saida.codigo = codigo
            saida.responsavel = responsavel

            saida.update()

            return saida.json(), 200

        else:
            return {"code status":"Dados invalidos"}, 400

    
    def patch(self, id):

        body = request.json()
        saida = Saida.query.get_or_404(id)
        
        produto = body.get("produto", saida.produto)
        codigo = body.get("codigo", saida.produto)
        #validade = body.get("validade", saida.validade)
        responsavel = body.get("responsavel", saida.responsavel)

        if isinstance(produto, str) and\
            isinstance(codigo, str) and\
                isinstance(responsavel, int):

            saida = Saida.query.filter_by(codigo=codigo).first()

            if saida:
                return   ("code status: Dados inválidos, saida já realizada"), 400
            
            saida.produto = produto
            saida.codigo = codigo
            saida.responsavel = responsavel

            saida.update()

            return saida.json(), 200

        #else:
        #    return {"code status":"Dados invalidos"}, 400
    
    def delete(self, id):

        saida = Saida.query.get_or_404(id)
        saida.delete(saida)

        return saida.json()
        

