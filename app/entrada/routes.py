from app.entrada.model import entrada_api
from app.entrada.controller import EntradaDetails, EntradaCreate

entrada_api.add_url_rule("/registro", view_func = EntradaCreate.as_view("cria entrada"), methods = ["POST","GET"])
entrada_api.add_url_rule("/modficar", view_func = EntradaDetails.as_view("modifica entrada"), methods = ["GET","PUT","PATCH", "DELETE"])

