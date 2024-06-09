# Variáveis globais
saldo_cc = 0.0
extratocc = ""

def deposito(valor):
    global saldo_cc
    global extratocc
    saldo_cc += valor
    extratocc += f"- Depósito efetuado no valor de R${valor:.2f}\n"

def saque(valor):
    global saldo_cc
    global extratocc
    if valor <= saldo_cc:
        saldo_cc -= valor
        extratocc += f"- Saque efetuado no valor de R${valor:.2f}\n"
    else:
        print("Saldo insuficiente para realizar o saque.")

def extrato():
    global extratocc
    print("Extrato da Conta Corrente:")
    print(extratocc)

def saldo():
    global saldo_cc
    print(f"Saldo atual: R${saldo_cc:.2f}")
