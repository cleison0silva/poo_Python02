class Cliente:                                #CLASSE CLIENTE

    def __init__(self, nome, cpf, idade):     #CONSTRUÇÃO DOS PARÂMETROS
        self.nome = nome
        self.cpf = cpf
        self.idade = idade

    def __str__(self):
        return "Nome: " + self.nome + "\nCPF: " + self.cpf + "\nIdade: " + str(self.idade)  #METÓDO PARA OTIMIZAR O PRINT