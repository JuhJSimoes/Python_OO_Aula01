
class Conta:
    def __init__(self, numero, titular, saldo, limite): #construtor em python
        print("Construindo objeto {}".format(self))
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
    
    
    def extrato_conta(self):
        print("Saldo {} do titular {}".format(self.__saldo, self.__titular))
        
    def deposita_conta(self, valor):
        self.__saldo += valor
        
    def __pode_saca(self, valor_sacar):
        valor_disponivel = self.__saldo + self.__limite
        return valor_sacar <= valor_disponivel
        
    def saca_conta(self, valor):
        if (self.__pode_saca(valor)):
            self.__saldo -= valor
        else:
            print("Valor {} passou o limite".format(valor))
            
        
    def transfere_conta(self, valor, destino):
        self.saca_conta(valor)
        destino.deposita_conta(valor)
    
    @property
    def saldo(self):
        return self.__saldo

    @property
    def titular(self):
        return self.__titular
    
    @property
    def numero(self):
        return self.__numero
    
    @property #get
    def limite(self):
        return self.__limite
    
    @limite.setter #set
    def limite(self, limite):
        self.__limite = limite
    
    @staticmethod
    def codigo_bancos():
        return {'BB': '001', 'CAIXA':'104', 'ITAU':'341'}