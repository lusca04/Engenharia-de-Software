from datetime import datetime

class Plano:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def mostrar(self):
        print(f"Plano: {self.nome} | R$ {self.preco:.2f}")


class Conteudo:
    def __init__(self, titulo, genero):
        self.titulo = titulo
        self.genero = genero


class Filme(Conteudo):
    def __init__(self, titulo, genero, duracao):
        super().__init__(titulo, genero)
        self.duracao = duracao

    def assistir(self):
        print(f"\nAssistindo filme: {self.titulo}")
        print(f"Gênero: {self.genero}")
        print(f"Duração: {self.duracao} min")


class Serie(Conteudo):
    def __init__(self, titulo, genero, temporadas):
        super().__init__(titulo, genero)
        self.temporadas = temporadas

    def assistir(self):
        print(f"\nAssistindo série: {self.titulo}")
        print(f"Gênero: {self.genero}")
        print(f"Temporadas: {self.temporadas}")


class Usuario:
    def __init__(self, nome):
        self.nome = nome
        self.plano = None

    def login(self):
        print(f"{self.nome} fez login na plataforma.")

    def assinar(self, plano):
        self.plano = plano
        print(f"{self.nome} assinou o plano {plano.nome}.")

    def assistir(self, conteudo):

        if self.plano == None:
            print("Você não possui assinatura.")
            return

        conteudo.assistir()

        print("Horário:", datetime.now().strftime("%d/%m/%Y %H:%M"))


# ---------------- TESTES ----------------

# planos
plano1 = Plano("Básico", 29.90)
plano2 = Plano("Premium", 55.90)

print("PLANOS")
plano1.mostrar()
plano2.mostrar()

# usuário
print("\n LOGIN")

usuario1 = Usuario("Ana")
usuario1.login()

# assinatura
print("\n ASSINATURA")

usuario1.assinar(plano2)

# conteúdos
filme1 = Filme("mad max", "tudo", 180)

serie1 = Serie("Narcos", "drogas", 5)

# assistir
print("\n FILME")
usuario1.assistir(filme1)

print("\n SÉRIE")
usuario1.assistir(serie1)