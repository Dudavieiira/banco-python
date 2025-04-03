#Novas funcionalidades:
#4- separar as funções existentes de saque, deposito e extrato em funções. Criar duas novas funçoes: cadastrar usuário (cliente) e cadastrar conta bancaria
#-devemos criar funções para todas as operações do sistema, cada funçaõ vai ter uma regra na passagem de argumentos
#-a função saque deve receber os argumentos apenas por nome (keyword only). argumentos: saldo, valor, limite, extrato, numero_saques e limite_saque. retorno: saldo, extrato e numero_saques.
#- a funçao deposito deve receber os argumentos apenas por posição (positional only). argumentos: saldo, valor, extrato. retorno: saldo e extrato
#- a função extrato deve receber os argumentos por posição e nome (positional only e keyword only). argumentos posicionais: saldo argumentos nomeados: extrato
#5- precisamos deixar o codigo mais modularizado, para isso vamos criar funções para as operações existentes: sacar, depositar e visualizar historico
#-alem disso para a versão 2 do nosso sistema precisamos criar duas novas funções, criar usuario (cliente do banco) e criar conta corrente (vincular com usuario)
#-criar usuario: deve armazenar os usuarios em uma lista, um usuario é composto por: nome, data de nascimento, cpf e endereço, o endereço é uma string com o formato: logradouro, nro - bairro - cidade/sigla estado. 
#deve ser armazenadp somente os numeros do cpf(string). não podemos cadastrar 2 usuariops com o mesmo cpf
#-criar conta corrente: o programa deve armazenar contas em uma lista, uma conta é composta por: agencia, numero da conta e usuario. o numero da conta é sequencial, iniciando em 1.
# o numero da agencia é fixo "0001" ex: 0001-1 dps 0001-2. o usuario pode ter mais de uma conta mas uma conta so pertence a um usuario.
#para vinculae aum usuario a uma conta, filtre a lista de usuarios buscando o numero do cpf informado para cada usuario da lista

import textwrap

def menu() : 
    menu = """\n
    ===================== MENU ====================
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova Conta
    [lc]\tListar Contas
    [nu]\tNovo Usuário
    [q]\tSair 
    ===============================================
    => """
    return input(textwrap.dedent(menu)) #utiliza o textwrap para formatar o menu, o input solicita a opção desejada pelo usuário

def depositar(saldo, valor, extrato, /):
    if valor > 0:  # se o valor for maior que 0, o deposito é válido
        saldo += valor  # soma o saldo ao valor do depósito
        extrato += f"Depósito: R$ {valor:.2f}\n"  # utiliza o float para formatar o valor com 2 casas decimais
        print("\n=== Depósito realizado com sucesso! ===")
    else:
        print("\n@@@ Operação falhou! O valor informado é inválido. @@@")

    return saldo, extrato  # retorna o saldo e o extrato atual

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo= valor > saldo #verifica se o valor do saque é maior que o saldo
    excedeu_limite= valor > limite #verifica se o valor do saque é maior que o limite       
    excedeu_saques= numero_saques >= limite_saques #verifica se o número de saques é maior que o limite de saques

    if excedeu_saldo:
        print("\n@@@ Operação falhou! Você não tem saldo suficiente. @@@")
    elif excedeu_limite:
        print("\n@@@ Operação falhou! O valor do saque excede o limite. @@@")
    elif excedeu_saques:
        print("\n@@@ Operação falhou! Número máximo de saques diários atingido. @@@")
    elif valor > 0: #se o valor se saque for maior que zero
        saldo -= valor #ele diminui do saldo o valor sacado
        extrato += f"Saque: R$ {valor:.2f}\n" #utiliza o float para formatar o valor com 2 casas decimais
        numero_saques += 1 #incrementa o número de saques, pois só é possível 3 saques
        print("\n=== Saque realizado com sucesso! ===")
    else:
         print("\n@@@ Operação falhou! O valor informado é inválido. @@@")

    return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):   
    print("===== EXTRATO =====")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("===================")

def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente números): ")
    usuario = filtrar_usuario(cpf, usuarios) #filtra o usuário pelo cpf

    if usuario:
        print("\n@@@ Já existe um usuário com esse CPF! @@@")
        return
    
    nome = input("Informe o nome do usuário: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data}_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco}) #adiciona o usuário na lista de usuários (dicionario)
    print("=== Usuário cadastrado com sucesso! ===")

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"]== cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf= input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n=== Conta criada com sucesso! ===")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario} #retorna um dicionário com as informações da conta
    
    print("\n@@@ Usuário não encontrado, fluxo de criação de conta encerrado! @@@")

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha)) #utiliza o textwrap para formatar a linha

def main():

    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "d":
            valor = float(input("Informe o valor do depósito: ")) #solicita o valor do depósito usando o float para permitir valores decimais

            saldo, extrato = depositar(saldo, valor, extrato) #passa o saldo atual, o valor do depósito e o extrato atual para a função depositar

        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))
            saldo, extrato = sacar (
                saldo=saldo, #passa o saldo atual
                valor=valor, #passa o valor do saque
                limite=limite, #passa o limite de saque
                extrato=extrato, #passa o extrato atual
                numero_saques=numero_saques, #passa o número de saques realizados
                limite_saques=LIMITE_SAQUES #passa o limite de saques
            )

        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato) #passa o saldo atual e o extrato atual para a função exibir_extrato

        elif opcao == "nu":
            criar_usuario(usuarios)

        elif opcao == "nc":
            numero_conta = len(contas) + 1 #cria o número da conta, que é o tamanho da lista de contas + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == "lc":
            listar_contas(contas)

        elif opcao == "q":
            print("O saldo da conta é de R$ {:.2f}".format(saldo)) #exibe o saldo atual       
            print("Saindo...")
            break

        else: 
            print("Operação inváçida, por favor selecione novamente a operação desejada.")

main()