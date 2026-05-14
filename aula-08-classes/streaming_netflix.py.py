# ============================================================
# 🎬 Plataforma de Streaming — Diagrama de Classes UML
# Demonstra: Associação, Agregação e Composição
# ============================================================


# ── Composição forte: Item só existe dentro de Pedido ───────
class Item:
    """
    - id: int
    - nome: String
    - valor: float
    + adicionarCarrinho()
    """
    _contador = 1

    def __init__(self, nome: str, valor: float):
        self.id    = Item._contador
        Item._contador += 1
        self.nome  = nome
        self.valor = valor

    def adicionar_carrinho(self):
        print(f" '{self.nome}' (R$ {self.valor:.2f}) adicionado ao carrinho.")

    def __repr__(self):
        return f"{self.nome} — R$ {self.valor:.2f}"


# ── Agregação: Restaurante existe independente do Pedido ────
class Restaurante:
    """
    - id: int
    - nome: String
    - endereco: String
    + enviarPedido()
    """
    _contador = 1

    def __init__(self, nome: str, endereco: str):
        self.id       = Restaurante._contador
        Restaurante._contador += 1
        self.nome     = nome
        self.endereco = endereco

    def enviar_pedido(self, pedido: "Pedido"):
        print(f"  [{self.nome}] Pedido #{pedido.id} recebido e enviado para preparo!")

    def __repr__(self):
        return f"{self.nome} ({self.endereco})"


# ── Associação: Cliente referencia Pedido ───────────────────
class Cliente:
    """
    - cadastro: int
    - nome: String
    - cpf: String
    + Comprar()
    """
    _contador = 1

    def __init__(self, nome: str, cpf: str):
        self.cadastro = Cliente._contador
        Cliente._contador += 1
        self.nome = nome
        self.cpf  = cpf

    def comprar(self, pedido: "Pedido"):
        print(f"\n{self.nome} está confirmando o pedido...")
        pedido.confirmar()

    def __repr__(self):
        return f"Cliente #{self.cadastro} — {self.nome}"


# ── Classe central: Pedido ───────────────────────────────────
class Pedido:
    """
    - id: int
    - status: String
    - total: float
    + confirmar()
    + calcularTotal()

    Composição com Item    (◆): itens criados/destruídos com o pedido
    Agregação com Restaurante (◇): restaurante existe independentemente
    """
    _contador = 1

    def __init__(self, restaurante: Restaurante):
        self.id          = Pedido._contador
        Pedido._contador += 1
        self.status      = "aberto"
        self.total       = 0.0
        self.restaurante = restaurante          # agregação ◇
        self.itens: list[Item] = []             # composição ◆

    def adicionar_item(self, nome: str, valor: float):
        """Cria o Item DENTRO do pedido — composição forte."""
        item = Item(nome, valor)                # item nasce aqui
        item.adicionar_carrinho()
        self.itens.append(item)

    def calcular_total(self) -> float:
        self.total = sum(item.valor for item in self.itens)
        return self.total

    def confirmar(self):
        if not self.itens:
            print("  Pedido vazio! Adicione itens antes de confirmar.")
            return

        self.calcular_total()
        self.status = "confirmado"
        print(f"  Pedido #{self.id} confirmado! Total: R$ {self.total:.2f}")
        self.restaurante.enviar_pedido(self)
        self.status = "em preparo"
        print(f"  Status: {self.status}")

    def __repr__(self):
        return (f"Pedido #{self.id} | Status: {self.status} | "
                f"Total: R$ {self.total:.2f} | Restaurante: {self.restaurante.nome}")


# ============================================================
# Sistema Netflix — Agregação + Associação
# ============================================================

class Avaliacao:
    """Criada pelo Usuário e associada a um Filme."""
    def __init__(self, nota: float, comentario: str):
        self.nota       = nota
        self.comentario = comentario

    def __repr__(self):
        return f"{self.nota}/10 — \"{self.comentario}\""


class Filme:
    """Existe independentemente de qualquer Catálogo ou Usuário."""
    def __init__(self, titulo: str, duracao: int, genero: str):
        self.titulo   = titulo
        self.duracao  = duracao   # minutos
        self.genero   = genero
        self.avaliacoes: list[Avaliacao] = []

    def receber_avaliacao(self, avaliacao: Avaliacao):
        self.avaliacoes.append(avaliacao)

    def media_notas(self) -> float:
        if not self.avaliacoes:
            return 0.0
        return sum(a.nota for a in self.avaliacoes) / len(self.avaliacoes)

    def __repr__(self):
        return f"{self.titulo} ({self.genero}, {self.duracao} min)"


class Catalogo:
    """
    Agregação com Filme (◇):
    filmes existem fora do catálogo e podem estar em vários catálogos.
    """
    def __init__(self, nome: str, ano: int):
        self.nome   = nome
        self.ano    = ano
        self.filmes: list[Filme] = []   # agregação ◇

    def add_filme(self, filme: Filme):
        self.filmes.append(filme)
        print(f"  '{filme.titulo}' adicionado ao catálogo '{self.nome}'.")

    def listar_filmes(self):
        print(f"\nCatálogo: {self.nome}")
        for filme in self.filmes:
            media = filme.media_notas()
            estrelas = f" | {media:.1f}" if media else ""
            print(f"  {filme}{estrelas}")


class Usuario:
    """
    Associação com Avaliacao (→):
    usuário referencia avaliações mas não as cria internamente.
    """
    def __init__(self, nome: str, email: str, plano: str):
        self.nome        = nome
        self.email       = email
        self.plano       = plano
        self.avaliacoes: list[tuple[Filme, Avaliacao]] = []

    def avaliar(self, filme: Filme, avaliacao: Avaliacao):
        filme.receber_avaliacao(avaliacao)
        self.avaliacoes.append((filme, avaliacao))
        print(f"  {self.nome} avaliou '{filme.titulo}': {avaliacao}")

    def ver_avaliacoes(self):
        print(f"\n Avaliações de {self.nome} ({self.plano}):")
        if not self.avaliacoes:
            print("  Nenhuma avaliação ainda.")
            return
        for filme, avaliacao in self.avaliacoes:
            print(f"  {filme.titulo}: {avaliacao}")


class Plataforma:
    """Composição com Catalogo (◆): catálogos pertencem à plataforma."""
    def __init__(self, nome: str, pais: str):
        self.nome      = nome
        self.pais      = pais
        self.catalogos: list[Catalogo] = []

    def add_catalogo(self, catalogo: Catalogo):
        self.catalogos.append(catalogo)

    def __repr__(self):
        return f"{self.nome} ({self.pais})"


# ============================================================
# 🧪 EXECUÇÃO — exatamente como o enunciado pede
# ============================================================

print("=" * 50)
print("SISTEMA DE PEDIDOS")
print("=" * 50)

restaurante = Restaurante("Pizza Napoli", "Av. Paulista, 1000")
pedido = Pedido(restaurante)
pedido.adicionar_item("Pizza Margherita", 49.90)
pedido.adicionar_item("Refrigerante 2L",  12.00)
pedido.adicionar_item("Sobremesa Tiramisu", 18.50)

cliente = Cliente("Carlos Souza", "123.456.789-00")
cliente.comprar(pedido)
print(f"\n{pedido}")

print("\n" + "=" * 50)
print("SISTEMA NETFLIX")
print("=" * 50)

netflix  = Plataforma("Netflix", "EUA")
catalogo = Catalogo("Filmes em Destaque", 0)

filme1 = Filme("Oppenheimer", 180, "Drama")
filme2 = Filme("Barbie",      114, "Comédia")

catalogo.add_filme(filme1)
catalogo.add_filme(filme2)
netflix.add_catalogo(catalogo)

usuario   = Usuario("Ana", "ana@email.com", "Premium")
avaliacao = Avaliacao(9.5, "Incrível! Assisti duas vezes")
usuario.avaliar(filme1, avaliacao)

catalogo.listar_filmes()
usuario.ver_avaliacoes()