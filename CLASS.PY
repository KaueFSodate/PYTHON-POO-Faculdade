class Pessoa:

    #Construtor da class Pessoa
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_nome(self):
        return self.nome
    
    def get_idade(self):
        return self.idade
    
    def set_nome(self, nome):
        self.nome = nome

    def set_idade(self, idade):
        self.idade = idade

    #Função de apresentar
    def apresentar(self):
        print(f"Olá, meu nome é {self.nome} e eu tenho {self.idade} anos.")

class Aluno(Pessoa):
    #Construtor da class Aluno
    def __init__(self, nome, idade, RA, curso):
        #Construtor da class Pessoa
        super().__init__(nome, idade)
        self.RA = RA
        self.curso = curso

    def get_RA(self):
        return self.RA
    
    def set_RA(self, RA):
        self.RA = RA

    def get_curso(self):
        return self.curso
    
    ## Função de alterar o curso
    def set_curso(self, curso):
        self.curso = curso

    def mostrar_curso(self):
        print(f"O meu curso eh: {self.curso}")


aluno = Aluno('Kaue', '19', '023031080', 'Análise e desenvolvimento de sistemas')

aluno.apresentar()

aluno.mostrar_curso()

aluno.set_curso('Sistemas de informação')

aluno.mostrar_curso()