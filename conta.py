class Conta:

    def __init__(self, numero, titular, saldo, limite):
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print("Saldo de R$ {}, do titular: {}".format(self.__saldo, self.__titular))

    def deposito(self, valor):
        self.__saldo += valor

    def saque(self, valor):
        if self.__pode_sacar(valor):
            self.__saldo -= valor
        else:
            print("Saldo insuficiente, saldo atual: {}".format(self.__saldo))

    def transferencia(self, conta, valor):
        if self.__saldo >= valor:
            self.saque(valor)
            conta.deposita(valor)
        else:
            print("Saldo insuficiente, saldo atual: {}".format(self.__saldo))

    def __pode_sacar(self, valor_a_sacar):
        valor_disponivel_a_sacar = self.__saldo + self.__limite
        return valor_a_sacar <= valor_disponivel_a_sacar

    @property
    def saldo(self):
        return self.__saldo

    @property
    def titular(self):
        return self.__titular

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, valor):
        self.__limite = valor @ staticmethod

    @staticmethod
    def codigos_bancos():
        return {'BB': '001', 'Caixa': '104', 'Itau': '341'}
