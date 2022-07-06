from app.saida.model import saida_api
from app.saida.controller import SaidaDetails, SaidaCreate

saida_api.add_url_rule("/registro", view_func = SaidaCreate.as_view("cria saida"), methods = ["POST","GET"])
saida_api.add_url_rule("/modficar", view_func = SaidaDetails.as_view("modifica saida"), methods = ["GET","PUT","PATCH", "DELETE"])

