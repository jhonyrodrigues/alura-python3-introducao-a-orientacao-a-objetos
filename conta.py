
class Conta:

    def __init__(self, numero, titular, saldo, limite):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite

    def extrato(self):
        print("Saldo de R$ {}, do titular: {}".format(self.saldo, self.titular))

    def deposita(self, valor):
        self.saldo += valor

    def saque(self, valor):
        if self.saldo > valor:
            self.saldo -= valor
        else:
            print("Saldo insuficiente, saldo atual: {}".format(self.saldo))

    def transferencia(self, conta, valor):
        if self.saldo > valor:
            self.saldo -= valor
            conta.saldo += valor
        else:
            print("Saldo insuficiente, saldo atual: {}".format(self.saldo))