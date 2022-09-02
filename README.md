# poo_Python02
Exercício 2 aulas de introdução a POO com Python

No segundo exercício de introdução à programação orientada a objeto vi como fazer uma pequena aplicação para cadastrar clientes e contas bancárias, usando métodos para realizar transferências básicas, como sacar, depositar e consultar saldo. Criei 3 arquivos, 2 objetos e o arquivo principal.

1º Arquivo: clientes.py, foi criada a classe Cliente onde teve como parâmetros Nome, CPF e idade, também foi construído um método para otimizar a visualização das informações, através do str.

2º Arquivo: contas.py, foi criada a classe Conta, com parâmetros de Cliente, Saldo e Limite negativo. Logo depois criei os métodos: Sacar, onde apenas pode ser realizado saques caso o valor não seja menor que o limite da conta do cliente. Depositar, método para incluir valor na conta com a condição que seja maior que 0 e por fim o método Consulta, onde o mesmo dá um return da classe saldo.

3º Arquivo: exercicio2.py

Fiz alguns testes com o código: inicialmente importei os dois objetos (linhas 3-4), logo depois passei os parâmetros dos objetos Clientes e Conta (linhas 8-9) usei o objeto Cliente como parâmetro para o objeto Conta. A partir da linha 18 inicie os testes das classes, DEPOSITAR: o programa não permitiu depositar valor negativo. SAQUE: o programa não permitiu sacar um valor maior que o limite da conta.
