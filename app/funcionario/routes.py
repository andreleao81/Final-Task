from app.funcionario.model import funcionario_api
from app.funcionario.controller import FuncionarioCreate, FuncionarioDetails, FuncionarioLogin

funcionario_api.add_url_rule("/registro", view_func = FuncionarioCreate.as_view("cria funcionario"), methods = ["POST","GET"])
funcionario_api.add_url_rule("/modficar", view_func = FuncionarioDetails.as_view("modifica funcionario"), methods = ["GET","PUT","PATCH", "DELETE"])
funcionario_api.add_url_rule("/login", view_func = FuncionarioLogin.as_view("login funcionario"), methods = ["POST"])
