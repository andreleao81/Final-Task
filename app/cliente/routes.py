from app.cliente.model import cliente_api
from app.cliente.controller import ClienteDetails, ClienteCreate

cliente_api.add_url_rule("/registro", view_func = ClienteCreate.as_view("cria cliente"), methods = ["POST","GET"])
cliente_api.add_url_rule("/modficar", view_func = ClienteDetails.as_view("modifica cliente"), methods = ["GET","PUT","PATCH", "DELETE"])

