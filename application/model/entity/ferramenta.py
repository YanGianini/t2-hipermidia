class Ferramenta():
    def __init__(self, nome, link, descricoes):
        self.__nome = nome
        self.__link = link
        self.__descricoes = descricoes
        self.__tags = []

    def get_nome(self):
        return self.__nome

    def set_nome(self, nome):
        self.__nome = nome


    def get_link(self):
        return self.__link
    
    def set_link(self, link):
        self.__link = link


    def get_descricoes(self):
        return self.__descricoes

    def set_descricoes(self, descricoes):
        self.__descricoes= descricoes


    def get_tags(self):
        return self.__tags

    def add_tag(self, tags):
        self.__tags.append(tags)