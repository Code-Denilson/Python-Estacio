# CCorrente.py

from Lib_CCorrente import deposito, saque, extrato, saldo

def main():
    while True:
        print("\n--- Conta Corrente ---")
        print("1. Depósito")
        print("2. Saque")
        print("3. Extrato")
        print("4. Saldo")
        print("5. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            valor = float(input("Digite o valor a ser depositado: "))
            deposito(valor)
        elif opcao == "2":
            valor = float(input("Digite o valor a ser sacado: "))
            saque(valor)
        elif opcao == "3":
            extrato()
        elif opcao == "4":
            saldo()
        elif opcao == "5":
            print("Fim do programa!")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
