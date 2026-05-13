# Classe usuário
class Usuario:

    def __init__(self, nome, email, senha):

        self.nome = nome
        self.email = email
        self.senha = senha
        self.ativo = False


# sistema
class Sistema:

    def __init__(self):

        self.usuarios = []

    # cadastrar usuário
    def cadastrar(self, nome, email, senha):

        # verificar campos vazios
        if nome == "" or email == "" or senha == "":
            print("Preencha todos os campos")
            return

        # verificar email
        if "@" not in email:
            print("Email inválido")
            return

        # verificar senha
        if len(senha) < 6:
            print("Senha muito curta")
            return

        # criar usuário
        usuario = Usuario(nome, email, senha)

        self.usuarios.append(usuario)

        print("Usuário cadastrado:", usuario.nome)

    # aprovar usuário
    def aprovar_usuario(self, email):

        for usuario in self.usuarios:

            if usuario.email == email:

                usuario.ativo = True

                print("Usuário aprovado:", usuario.nome)

    # listar usuários
    def listar_usuarios(self):

        print("\nUSUÁRIOS")

        for usuario in self.usuarios:

            if usuario.ativo == True:
                status = "Ativo"
            else:
                status = "Pendente"

            print(usuario.nome, "-", status)


# sistema
sistema = Sistema()

# Cadastros
sistema.cadastrar("Ana", "ana@email.com", "123456")

sistema.cadastrar("Carlos", "carlosemail.com", "123456")

sistema.cadastrar("Maria", "maria@email.com", "123")

sistema.cadastrar("", "teste@email.com", "123456")

# Aprovação
print("\nAPROVAÇÃO")

sistema.aprovar_usuario("ana@email.com")

# Mostrar usuários
sistema.listar_usuarios()