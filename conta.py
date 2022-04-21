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
        if self.__saldo >= valor:
            self.__saldo -= valor
        else:
            print("Saldo insuficiente, saldo atual: {}".format(self.__saldo))

    def transferencia(self, conta, valor):
        if self.__saldo >= valor:
            self.saque(valor)
            conta.deposita(valor)
        else:
            print("Saldo insuficiente, saldo atual: {}".format(self.__saldo))

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
        self.__limite = valor
