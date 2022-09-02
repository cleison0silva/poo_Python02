#importando os objetos

from clientes import Cliente
from contas import Contas

print("####EXERCÍCIO CONTA BANCÁRIA###\n")

cliente1 = Cliente("Cleison", "123.456.789-10", 28) #passando os parâmetros do cliente 1.
conta_cliente1 = Contas(cliente1,100,-50)           #vinculando o cliente 1 a sua conta.

#consultando o cadastro do cliente

print("Cliente 1")
print(conta_cliente1)

print("\nxxxxxxxxxxxxxxxxxx\n")

#Realizando Depósito

print("Consulta: ", conta_cliente1.consulta())

print("\nDEPOSITAR\n")

conta_cliente1.depositar(-10) #valor negativo não depositado
conta_cliente1.depositar(50)  #deposito realizado

print("\nConsulta: ", conta_cliente1.consulta())

#Realizando Saque

print("\nSACAR\n")

conta_cliente1.sacar(200)  #saque realizado

print("\nConsulta: ", conta_cliente1.consulta())

conta_cliente1.sacar(100) #saque maior que o limite, saque não realizado