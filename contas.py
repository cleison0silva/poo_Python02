class Contas:                                     #CLASSE CONTAS

    def __init__(self, cliente, saldo, limite):   #CONTRUÇÃO DOS PARÂMETROS
        self.cliente = cliente
        self.saldo = saldo
        self.limite = limite

    def sacar(self, saque):                       #METÓDO PARA REALIZAR O SAQUE, COM UMA CONDIÇÃO QUE NÃO SEJA REALIZADO MENOR QUE O LIMITE DA CONTA.
        if self.saldo - saque < self.limite:
            print("SALDO INSUFICIENTE")
        else:
            self.saldo -= saque
            print("Foi Retirado:", saque)

    def depositar(self, deposito):                #METÓDO PARA REALIZAR O DEPÓSITO DA CONTA, CASO O VALOR PASSADO SEJA MAIOR QUE 0
        if deposito > 0:
            self.saldo += deposito
            print("Foi depositado: ", deposito)
        else:
            print("Erro no Deposito")

    def consulta(self):                           #METÓDO PARA REALIZAR A CONSULTA DO SALDO
        return self.saldo

    def __str__(self):
        return str(self.cliente) + "\nSaldo: " + str(self.saldo) + "\nLimite: " + str(self.limite)   #METÓDO PARA OTIMIZAR O PRINT

