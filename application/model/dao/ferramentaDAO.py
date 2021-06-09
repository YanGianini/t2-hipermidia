from typing import List
from application.model.entity.ferramenta import Ferramenta

ferramenta1 = Ferramenta("Todo mvc", "linkzin", "mvc do professor com estrutura mvc")
ferramenta2 = Ferramenta("T2 tassio lindo", "link lindo", "nosso lindo professor pediu para que façamos trabalho liindo")

ferramenta1.add_tag("tarefa")
ferramenta1.add_tag("organização")

ferramenta2.add_tag("beleza")
ferramenta2.add_tag("diverção")

ferramenta_list = [ferramenta1, ferramenta2]

class FerramentaDAO():
    def __init__(self):
       self.ferramenta_list = ferramenta_list

    def lista_ferramentas(self):
        return self.ferramenta_list