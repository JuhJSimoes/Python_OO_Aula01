class Cliente:
    def __init__(self, nome):
        self.__nome = nome

    @property # é o get em python
    def nome(self):
        return self.__nome.title()
    
    @nome.setter #é o set em python
    def nome(self, nome):
        self.__nome = nome 