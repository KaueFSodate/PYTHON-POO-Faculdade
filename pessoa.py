class Pessoa:

    #Construtor da class Pessoa
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    #Função de apresentar
    def apresentar(self):
        print(f"Olá, meu nome é {self.nome} e eu tenho {self.idade} anos.")

# Criando uma instância da classe Pessoa
pessoa1 = Pessoa("João", 25)

# Chamando o método apresentar()
pessoa1.apresentar()

#Herança da class Pessoa

class Aluno(Pessoa):
    #Construtor da class Aluno
    def __init__(self, nome, idade, matricula):
        #Construtor da class Pessoa
        super().__init__(nome, idade)
        self.matricula = matricula

    def estudar(self):
        print(f"{self.nome} está estudando.")

# Criando uma instância da classe Aluno
aluno = Aluno("João", 20, "12345")

# Chamando o método apresentar() da classe Pessoa (herdado pela classe Estudante)
aluno.apresentar()

# Acessando o atributo matricula da classe Estudante
print(f"Matrícula: {estudante.matricula}")

# Chamando o método estudar() da classe Estudante
estudante.estudar()

class Cachorro:
    #Construtor da class Pessoa
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    #Função de latir
    def latir(self):
        print(f"{self.nome}: Au au!")

# Criando uma instância da classe Cachorro
cachorro1 = Cachorro("Rex", 3)

# Chamando o método latir()
cachorro1.latir()


class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.lido = False

    def marcar_como_lido(self):
        self.lido = True

# Criando uma instância da classe Livro
livro1 = Livro("Dom Casmurro", "Machado de Assis")

# Acessando os atributos do livro
print(f"Título: {livro1.titulo}")
print(f"Autor: {livro1.autor}")

# Chamando o método marcar_como_lido()
livro1.marcar_como_lido()

# Verificando se o livro foi lido
if livro1.lido:
    print("Este livro foi lido.")
else:
    print("Este livro ainda não foi lido.")


