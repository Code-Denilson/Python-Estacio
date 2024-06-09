#Importação das datas atuais do computador.
from datetime import datetime 

#Tratamento da variavel de Depósito
def deposito(valor, saldo, extratocc): 
    saldo += valor
    extratocc.append(f"{datetime.now().strftime('%d/%m/%Y %H:%M:%S')} - Depósito efetuado no valor de R${valor:.2f}")
    return saldo, extratocc

#Tratamento da variavel de Saque
def saque(valor, saldo, extratocc): 
    if valor <= saldo:
        saldo -= valor
        extratocc.append(f"{datetime.now().strftime('%d/%m/%Y %H:%M:%S')} - Saque efetuado no valor de R${valor:.2f}")
        print(f"Saque efetuado no valor de R${valor:.2f}")
    else:
        print("Saldo insuficiente para realizar o saque.")
    return saldo, extratocc

#Tratamento da variavel do Extrato
def extrato(extratocc):
    print("Extrato da Conta Corrente:")
    for linha in extratocc:
        print(linha)

#Tratamento da variavel de Saldo
def saldo(saldo):
    print(f"Saldo atual: R${saldo:.2f}")
