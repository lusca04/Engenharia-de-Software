# Classe livro
class Livro:

    def __init__(self, titulo):

        self.titulo = titulo
        self.disponivel = True


# Classe usuário
class Usuario:

    def __init__(self, nome):

        self.nome = nome


# Classe biblioteca
class Biblioteca:

    def __init__(self):

        self.livros = []

    # adicionar livro
    def adicionar_livro(self, livro):

        self.livros.append(livro)

        print("Livro adicionado:", livro.titulo)

    # emprestar livro
    def emprestar_livro(self, usuario, livro):

        if livro.disponivel == True:

            livro.disponivel = False

            print(usuario.nome, "pegou o livro", livro.titulo)

        else:

            print("Livro não disponível")

    # devolver livro
    def devolver_livro(self, livro):

        livro.disponivel = True

        print("Livro devolvido:", livro.titulo)


# Criando biblioteca
biblioteca = Biblioteca()

# Criando livros
livro1 = Livro("1984")
livro2 = Livro("Dom Casmurro")

# Criando usuários
usuario1 = Usuario("Ana")
usuario2 = Usuario("Carlos")

# Adicionando livros
biblioteca.adicionar_livro(livro1)
biblioteca.adicionar_livro(livro2)

print("\nEMPRÉSTIMO")

# Empréstimo
biblioteca.emprestar_livro(usuario1, livro1)

# Tentando pegar o mesmo livro
biblioteca.emprestar_livro(usuario2, livro1)

print("\nDEVOLUÇÃO")

# Devolução
biblioteca.devolver_livro(livro1)

# Empréstimo novamente
biblioteca.emprestar_livro(usuario2, livro1)