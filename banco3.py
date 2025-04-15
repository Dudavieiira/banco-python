from abc import ABC, abstractclassmethod, abstractproperty, abstractmethod
from datetime import datetime


# Classe que representa um cliente genérico do banco
class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco  # Endereço do cliente
        self.contas = []  # Lista de contas associadas ao cliente

    # Método para realizar uma transação em uma conta específica
    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)  # Registra a transação na conta

    # Método para adicionar uma conta à lista de contas do cliente
    def adicionar_conta(self, conta):
        self.contas.append(conta)


# Classe que representa um cliente pessoa física, herda de Cliente
class PessoaFisica(Cliente):
    def __init__(self, nome, data_nascimento, cpf, endereco):
        super().__init__(endereco)  # Inicializa o endereço usando a classe base
        self.nome = nome  # Nome do cliente
        self.data_nascimento = data_nascimento  # Data de nascimento do cliente
        self.cpf = cpf  # CPF do cliente


# Classe que representa uma conta bancária genérica
class Conta:
    def __init__(self, numero, cliente):
        self._saldo = 0  # Saldo inicial da conta
        self._numero = numero  # Número da conta
        self._agencia = "0001"  # Agência fixa
        self._cliente = cliente  # Cliente associado à conta
        self._historico = Historico()  # Histórico de transações da conta

    # Método de classe para criar uma nova conta
    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(numero, cliente)

    # Propriedade para acessar o saldo da conta
    @property
    def saldo(self):
        return self._saldo

    # Propriedade para acessar o número da conta
    @property
    def numero(self):
        return self._numero

    # Propriedade para acessar a agência da conta
    @property
    def agencia(self):
        return self._agencia

    # Propriedade para acessar o cliente associado à conta
    @property
    def cliente(self):
        return self._cliente

    # Propriedade para acessar o histórico de transações da conta
    @property
    def historico(self):
        return self._historico

    # Método para realizar um saque na conta
    def sacar(self, valor):
        saldo = self.saldo  # Obtém o saldo atual
        excedeu_saldo = valor > saldo  # Verifica se o valor do saque excede o saldo

        if excedeu_saldo:
            print("\n@@@ Operação falhou! Você não tem saldo suficiente. @@@")
        elif valor > 0:  # Verifica se o valor do saque é válido
            self._saldo -= valor  # Deduz o valor do saldo
            print("\n=== Saque realizado com sucesso! ===")
            return True
        else:
            print("\n@@@ Operação falhou! O valor informado é inválido. @@@")

        return False

    # Método para realizar um depósito na conta
    def depositar(self, valor):
        if valor > 0:  # Verifica se o valor do depósito é válido
            self._saldo += valor  # Adiciona o valor ao saldo
            print("\n=== Depósito realizado com sucesso! ===")
        else:
            print("\n@@@ Operação falhou! O valor informado é inválido. @@@")
            return False

        return True


# Classe que representa uma conta corrente, herda de Conta
class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite=500, limite_saques=3):
        super().__init__(numero, cliente)  # Inicializa os atributos da classe base
        self.limite = limite  # Limite de saque por transação
        self.limite_saques = limite_saques  # Número máximo de saques permitidos por dia

    # Método para realizar um saque com regras específicas de conta corrente
    def sacar(self, valor):
        numero_saques = len(
            [transacao for transacao in self.historico.transacoes if transacao["tipo"] == Saque.__name__]
        )  # Conta o número de saques realizados

        excedeu_limite = valor > self.limite  # Verifica se o valor excede o limite
        excedeu_saques = numero_saques >= self.limite_saques  # Verifica se o número de saques foi excedido

        if excedeu_limite:
            print("\n@@@ Operação falhou! O valor do saque excede o limite. @@@")
        elif excedeu_saques:
            print("\n@@@ Operação falhou! Número máximo de saques excedido. @@@")
        else:
            return super().sacar(valor)  # Chama o método sacar da classe base

        return False

    # Método para exibir informações da conta corrente
    def __str__(self):
        return f"""\ 
            Agência:\t{self.agencia}
            C/C:\t\t{self.numero}
            Titular:\t{self.cliente.nome}
        """


# Classe que representa o histórico de transações de uma conta
class Historico:
    def __init__(self):
        self._transacoes = []  # Lista de transações realizadas

    # Propriedade para acessar as transações
    @property
    def transacoes(self):
        return self._transacoes

    # Método para adicionar uma transação ao histórico
    def adicionar_transacao(self, transacao):
        self._transacoes.append(
            {
                "tipo": transacao.__class__.__name__,  # Tipo da transação (Saque ou Depósito)
                "valor": transacao.valor,  # Valor da transação
                "data": datetime.now().strftime("%d-%m-%Y %H:%M:%s"),  # Data e hora da transação
            }
        )


# Classe abstrata que define a estrutura para transações
class Transacao(ABC):
    @property
    @abstractmethod
    def valor(self):
        pass  # Propriedade abstrata para obter o valor da transação

    @classmethod
    @abstractmethod
    def registrar(self, conta):
        pass  # Método abstrato para registrar a transação em uma conta


# Classe que representa uma transação de saque
class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor  # Valor do saque

    @property
    def valor(self):
        return self._valor

    # Método para registrar o saque em uma conta
    def registrar(self, conta):
        sucesso_transacao = conta.sacar(self.valor)  # Realiza o saque

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)  # Adiciona o saque ao histórico


# Classe que representa uma transação de depósito
class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor  # Valor do depósito

    @property
    def valor(self):
        return self._valor

    # Método para registrar o depósito em uma conta
    def registrar(self, conta):
        sucesso_transacao = conta.depositar(self.valor)  # Realiza o depósito

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)  # Adiciona o depósito ao histórico