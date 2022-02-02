
def cria_conta(numero, titular, saldo, limite):
    conta = {"numero": numero, "titular": titular, "saldo": saldo, "limite": limite}
    return conta

def deposita_conta(conta, valor):
    conta["saldo"] += valor
    
def saca_conta(conta, valor):
    conta["saldo"]  -= valor
    
def extrato_conta(conta):
    print("O saldo é {} ". format(conta["saldo"]))