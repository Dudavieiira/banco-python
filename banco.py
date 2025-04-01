# criar um sistema bancário

# 1-deve swer possível deopositar valores positivos para minha conta bancária. A v1 do projeto trabalha apenas com um usuário, 
# dessa forma não precisamos nos preocupar em identificar qual é o numero da agencia e conta bancaria. Todos os depositos
# devem ser armazenados em uma variavel e exibidos na operação de extrato.

# 2- o sistema deve permitir realizar 3 saques diários com limite máximo de 500,oo por saque. Caso o usuario não tenha saldo em conta, o sistema deve exibir uma
#mensagem informando que não há saldo suficiente. Todos os saques devem ser armazenados em uma variavel e exibidos na operação de extrato.

# 3- essa operação deve listar todos os depositos e saques realizados na conta. no fim da listagem deve ser exibido o saldo atual da conta. os valores
#devem ser exibidos utilizando o formato R$ xx.

menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair 

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: ")) #solicita o valor do depósito usando o float para permitir valores decimais
        if valor > 0: #se o valor for maior que 0, o deposito é válido
            saldo += valor #soma o saldo ao valor do depósito
            extrato += f"Depósito: R$ {valor:.2f}\n" #utiliza o float para formatar o valor com 2 casas decimais
        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))
        if valor > saldo:
            print("Operação falhou! Você não tem saldo suficiente.")
        elif valor > limite:
            print("Operação falhou! O valor do saque excede o limite.")
        elif numero_saques >= LIMITE_SAQUES:
            print("Operação falhou! Número máximo de saques diários atingido.")
        elif valor > 0: #se o valor se saque for maior que zero
            saldo -= valor #ele diminui do saldo o valor sacado
            extrato += f"Saque: R$ {valor:.2f}\n" #utiliza o float para formatar o valor com 2 casas decimais
            numero_saques += 1 #incrementa o número de saques, pois só é possível 3 saques
        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "e":
        print("===== EXTRATO =====")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("===================")

    elif opcao == "q":
        print("O saldo da conta é de R$ {:.2f}".format(saldo)) #exibe o saldo atual       
        print("Saindo...")
        break

else: 
    print("Operação inváçida, por favor selecione novamente a operação desejada.")