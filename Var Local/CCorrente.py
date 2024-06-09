# Para importar tudo da Lib se utilizar ( * ) ou informar quais variaveis importar

from Lib_CCorrente import deposito, saque, extrato, saldo # De LibCorrente importar .....

def main():
    saldo_cc = 0.0
    extratocc = []

    while True:
        try:
            print("\n--- Conta Corrente ---")
            print("1. Depósito")
            print("2. Saque")
            print("3. Extrato")
            print("4. Saldo")
            print("5. Sair")
            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                valor = float(input("\n Digite o valor a ser depositado: "))
                saldo_cc, extratocc = deposito(valor, saldo_cc, extratocc)
            elif opcao == "2":
                valor = float(input("\n Digite o valor a ser sacado: "))
                saldo_cc, extratocc = saque(valor, saldo_cc, extratocc)
            elif opcao == "3":
                extrato(extratocc)
            elif opcao == "4":
                saldo(saldo_cc)
            elif opcao == "5":
                print("Fim do programa!")
                break
            else:
                print("Opção inválida. Tente novamente.") #Inicio dos tratamentos de erros
        except ValueError:
            print("Entrada inválida. Por favor, digite um número válido.") #Erro referente a valores de opções inválidos
        except Exception as e:
            print(f"Ocorreu um erro: {e} entre em contato com a equipe de Ti.") #Erro de possíveis erros ocultos ou inesperados

if __name__ == "__main__": #Definir qual arquivo será o principal executador do projeto.
    main()
