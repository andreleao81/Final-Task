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

            entrada = Entrada.query.filter_by(codigo=codigo).first()

            if entrada:
                return   {"code status":"Dados inválidos, entrada já realizada"}, 400
            
            entrada = Entrada(produto = produto,\
                            codigo = codigo, \
                                responsavel = responsavel)

            entrada.save()

        return entrada.json(), 200


    def get(self):

        entradas = Entrada.query.all()

        return jsonify([entrada.json() for entrada in entradas]), 200

    
class EntradaDetails(MethodView):

    def get(self, id):
        
        entrada = Entrada.query.get_or_404(id)

        return entrada.json()
    
    def put(self, id):

        body = request.json()
        
        produto = body.get("produto")
        codigo = body.get("codigo")
        #incluir data de modificação
        responsavel = body.get("responsavel")

        if isinstance(produto, str) and\
            isinstance(codigo, str) and\
                isinstance(responsavel, int):

            entrada = Entrada.query.filter_by(codigo=codigo).first()

            if entrada:
                return   ("code status: Dados inválidos, entrada já realizada"), 400
            
            entrada.produto = produto
            entrada.codigo = codigo
            entrada.responsavel = responsavel


            entrada.update()

            return entrada.json(), 200

        else:
            return {"code status":"Dados invalidos"}, 400

    
    def patch(self, id):

        body = request.json()
        entrada = Entrada.query.get_or_404(id)
        
        produto = body.get("produto", Entrada.produto)
        codigo = body.get("codigo", Entrada.produto)
        #validade = body.get("validade", Entrada.validade)
        responsavel = body.get("responsavel", Entrada.responsavel)

        if isinstance(produto, str) and\
            isinstance(codigo, str) and\
                isinstance(responsavel, int):

            entrada = Entrada.query.filter_by(codigo=codigo).first()

            if entrada:
                return   ("code status: Dados inválidos, entrada já realizada"), 400
            
            entrada.produto = produto
            entrada.codigo = codigo
            entrada.responsavel = responsavel

            entrada.update()

            return entrada.json(), 200

        #else:
        #    return {"code status":"Dados invalidos"}, 400
    
    def delete(self, id):

        entrada = Entrada.query.get_or_404(id)
        entrada.delete(entrada)

        return entrada.json()
        

