from typing import List
from application.model.entity.ferramenta import Ferramenta

ferramenta1 = Ferramenta("Todo mvc", "linkzin", "mvc do professor com estrutura mvc")

ferramenta1.add_tag("tarefa")
ferramenta1.add_tag("organização")


ferramenta_list = [ferramenta1]

class FerramentaDAO():
    def __init__(self):
       self.ferramenta_list = ferramenta_list

    def lista_ferramentas(self):
        return self.ferramenta_list