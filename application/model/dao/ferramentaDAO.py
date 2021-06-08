from typing import List
from application.model.entity.ferramenta import Ferramenta

ferramenta_list = ["machado", "martelokk"]

class FerramentaDAO():
    def __init__(self):
       self.ferramenta_list = ferramenta_list

    def lista_ferramentas(self):
        return self.ferramenta_list