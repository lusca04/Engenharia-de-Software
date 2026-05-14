# ============================================================
# 🚀 DESAFIO EXTRA — versão OOP
# Cada classe representa uma entidade do seu diagrama UML
# ============================================================

class Livro:
    def __init__(self, titulo, autor):
        self.titulo     = titulo
        self.autor      = autor
        self.disponivel = True          # estado inicial

    def __repr__(self):
        status = "✅" if self.disponivel else "❌"
        return f"[{status}] {self.titulo} — {self.autor}"


class Biblioteca:
    def __init__(self):
        self.catalogo    = []
        self.emprestimos = {}           # { nome_leitor: [livros] }

    # UC-01: Cadastrar Livro
    def cadastrar(self, titulo, autor):
        self.catalogo.append(Livro(titulo, autor))
        print(f"📚 '{titulo}' cadastrado!")

    # UC-02: Listar Catálogo
    def listar(self):
        print("\n📖 Catálogo:")
        for livro in self.catalogo:
            print(f"  {livro}")

    # ── Método auxiliar privado ──────────────────────────────
    def _buscar_livro(self, titulo) -> "Livro | None":
        """Retorna o objeto Livro pelo título ou None se não existir."""
        for livro in self.catalogo:
            if livro.titulo == titulo:
                return livro
        return None

    # UC-03: Emprestar Livro ✅
    def emprestar(self, titulo, leitor):
        # <<include>> UC verificar disponibilidade — sempre ocorre
        livro = self._buscar_livro(titulo)

        if livro is None:
            print(f"❌ '{titulo}' não encontrado no catálogo.")
            return

        if not livro.disponivel:
            # Fluxo de exceção
            print(f"⚠️  '{titulo}' já está emprestado!")
            return

        # Fluxo principal: atualiza estado e registra empréstimo
        livro.disponivel = False

        # Cria a entrada do leitor se ainda não existir
        if leitor not in self.emprestimos:
            self.emprestimos[leitor] = []
        self.emprestimos[leitor].append(livro)

        print(f"✅ '{titulo}' emprestado para {leitor}!")

    # UC-04: Devolver Livro ✅
    def devolver(self, titulo, leitor):
        # Verifica se o leitor tem algum empréstimo ativo
        if leitor not in self.emprestimos or not self.emprestimos[leitor]:
            print(f"❌ {leitor} não possui empréstimos ativos.")
            return

        # Procura o livro específico na lista de empréstimos do leitor
        livro_devolvido = None
        for livro in self.emprestimos[leitor]:
            if livro.titulo == titulo:
                livro_devolvido = livro
                break

        if livro_devolvido is None:
            # Fluxo de exceção
            print(f"❌ '{titulo}' não consta nos empréstimos de {leitor}.")
            return

        # Fluxo principal: restaura disponibilidade e remove registro
        livro_devolvido.disponivel = True
        self.emprestimos[leitor].remove(livro_devolvido)

        # Limpa a chave do leitor se não tiver mais empréstimos
        if not self.emprestimos[leitor]:
            del self.emprestimos[leitor]

        print(f"✅ '{titulo}' devolvido por {leitor}!")

        # <<extend>> UC-05: Multa — comportamento opcional/condicional
        houve_atraso = input("  ⏰ Devolução atrasada? (s/n): ").strip().lower()
        if houve_atraso == "s":
            print("  📋 Multa aplicada!")


# ============================================================
# --- Teste da versão OOP ---
# ============================================================
bib = Biblioteca()
bib.cadastrar("Clean Code", "Robert C. Martin")
bib.cadastrar("Design Patterns", "Gang of Four")
bib.listar()

bib.emprestar("Clean Code", "Ana Silva")
bib.listar()

bib.devolver("Clean Code", "Ana Silva")
bib.listar()

# ---- Testes dos fluxos de exceção ----
print("\n--- Testes de exceção ---")
bib.emprestar("Livro Inexistente", "Ana Silva")   # livro não existe
bib.emprestar("Clean Code", "Ana Silva")          # empresta
bib.emprestar("Clean Code", "Carlos")            # já emprestado
bib.devolver("Design Patterns", "Ana Silva")      # livro não está com ela