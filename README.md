# Python-Estacio

### Documentação do Projeto Conta Corrente

#### Informações do Aluno
- **Nome:** [Denilson Araujo]
- **Número de Matrícula:** [202302196111]
- **Campus:** [Estácio - Maracanã]
- **Curso:** [Gestão da Tecnologia da Informação]
- **Turno:** [Noturno]
- **Professor:** [Lázaro Pereira]

---

#### Projeto: Programa Conta Corrente

#### Objetivo
Desenvolver um programa em Python denominado `ContaCorrente.py` que simula operações bancárias básicas (depósito, saque, consulta de saldo e extrato) com a utilização de funções.
Seguindo o que foi pedido no arquivo denominado "Enunciado do projeto.pdf".

---

#### Estrutura do Projeto
O projeto foi dividido em dois arquivos principais:
1. `Lib_CCorrente.py`: Contém as funções para realizar as operações bancárias.
2. `CCorrente.py`: Contém o programa chamador que interage com o usuário e utiliza as funções definidas em `Lib_CCorrente.py`.

#### Funcionalidades Implementadas

1. **Função de Depósito (`deposito`)**
   - **Descrição:** Incrementa o valor do depósito no saldo da conta corrente e registra a operação no extrato.
   - **Parâmetros:**
     - `valor` (float): Valor a ser depositado.
     - `saldo` (float): Saldo atual da conta.
     - `extratocc` (list): Lista de transações realizadas.
   - **Retorno:** Novo saldo e extrato atualizado.

2. **Função de Saque (`saque`)**
   - **Descrição:** Decrementa o valor do saque no saldo da conta corrente (se houver saldo suficiente) e registra a operação no extrato.
   - **Parâmetros:**
     - `valor` (float): Valor a ser sacado.
     - `saldo` (float): Saldo atual da conta.
     - `extratocc` (list): Lista de transações realizadas.
   - **Retorno:** Novo saldo e extrato atualizado.

3. **Função de Extrato (`extrato`)**
   - **Descrição:** Exibe o histórico de transações realizadas na conta corrente.
   - **Parâmetros:**
     - `extratocc` (list): Lista de transações realizadas.
   - **Retorno:** Nenhum.

4. **Função de Saldo (`saldo`)**
   - **Descrição:** Exibe o saldo atual da conta corrente.
   - **Parâmetros:**
     - `saldo` (float): Saldo atual da conta.
   - **Retorno:** Nenhum.

#### Conclusão

Este projeto foi desenvolvido para aplicar conceitos básicos de programação em Python, tais como uso de funções, tratamento de exceções, manipulação de listas e interação com o usuário. A separação das funcionalidades em dois arquivos (`Lib_CCorrente.py` e `CCorrente.py`) visa melhorar a modularidade e a organização do código. Este projeto foi realizado como parte da disciplina de [Paradigmas de Linguagens de Programação em Python] do curso de [Gestão da Tecnologia da Informação] na Estácio.
Sendo asssim, estando de acordo com o enunciado pedido pelo professor { Lázaro Pereira ] e entregue conforme o cronograma pedido.
---
