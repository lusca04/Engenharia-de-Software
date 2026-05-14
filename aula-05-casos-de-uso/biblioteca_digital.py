# ============================================================
# 🏛️ SISTEMA DE BIBLIOTECA DIGITAL — Biblioteca FIAP
# Cada seção = um Caso de Uso do diagrama que você fez no Miro
# ============================================================

# ----------------------------
# 📦 DADOS DO SISTEMA
# ----------------------------
catalogo = [
    {"titulo": "Clean Code",               "autor": "Robert C. Martin", "disponivel": True},
    {"titulo": "The Pragmatic Programmer", "autor": "Hunt & Thomas",    "disponivel": True},
    {"titulo": "Design Patterns",          "autor": "Gang of Four",     "disponivel": True},
]
emprestimos = []   # lista de {"leitor": ..., "livro": ..., "atrasado": bool}


# ============================================================
# UC-01: LISTAR CATÁLOGO
# Ator: Leitor
# ============================================================
print("📚 Catálogo disponível:")
for livro in catalogo:
    status = "✅" if livro["disponivel"] else "❌"
    print(f"  {status} {livro['titulo']} — {livro['autor']}")


# ============================================================
# UC-02: BUSCAR LIVRO  ✅ IMPLEMENTADO
# Ator: Leitor
# Pré-condição: catálogo não vazio
# ============================================================
print("\n🔍 Buscando livro...")
busca = "clean"   # o leitor digitou isso

# Percorre o catálogo comparando em minúsculas (case-insensitive)
resultados = [
    livro for livro in catalogo
    if busca.lower() in livro["titulo"].lower()
]

if resultados:
    print(f"  Resultados para '{busca}':")
    for livro in resultados:
        status = "✅ Disponível" if livro["disponivel"] else "❌ Indisponível"
        print(f"    • {livro['titulo']} — {livro['autor']} [{status}]")
else:
    print(f"  Nenhum livro encontrado para '{busca}'.")


# ============================================================
# UC-03: EMPRESTAR LIVRO
# Ator: Leitor
# <<include>> UC-04 Verificar Disponibilidade
# ============================================================
print("\n📌 Empréstimo:")
leitor = "Ana Silva"
titulo = "Clean Code"

# <<include>> — verificar disponibilidade (sempre acontece)
livro_encontrado = None
for livro in catalogo:
    if livro["titulo"] == titulo:
        livro_encontrado = livro
        break

if livro_encontrado is None:
    print("❌ Livro não encontrado no catálogo.")
elif livro_encontrado["disponivel"] == False:
    # Fluxo de exceção
    print(f"⚠️  '{titulo}' já está emprestado!")
else:
    # Fluxo principal
    livro_encontrado["disponivel"] = False
    emprestimos.append({"leitor": leitor, "livro": titulo, "atrasado": False})
    print(f"✅ '{titulo}' emprestado para {leitor}!")


# ============================================================
# UC-04: DEVOLVER LIVRO  ✅ IMPLEMENTADO
# Ator: Leitor
# <<extend>> UC-05 Aplicar Multa (só se atrasado)
# ============================================================
print("\n🔄 Devolução:")
leitor_devolvendo = "Ana Silva"
titulo_devolvendo = "Clean Code"

# Passo 1: procura o registro de empréstimo correspondente
registro_encontrado = None
for registro in emprestimos:
    if registro["leitor"] == leitor_devolvendo and registro["livro"] == titulo_devolvendo:
        registro_encontrado = registro
        break

if registro_encontrado is None:
    # Fluxo de exceção: empréstimo não existe
    print(f"❌ Nenhum empréstimo ativo de '{titulo_devolvendo}' para {leitor_devolvendo}.")
else:
    # Passo 2: marca o livro como disponível no catálogo
    for livro in catalogo:
        if livro["titulo"] == titulo_devolvendo:
            livro["disponivel"] = True
            break

    # Remove o registro da lista de empréstimos
    emprestimos.remove(registro_encontrado)
    print(f"✅ '{titulo_devolvendo}' devolvido por {leitor_devolvendo}!")

    # <<extend>> UC-05: Aplicar Multa — só ocorre se houve atraso
    # Em um sistema real isso viria de uma data; aqui simulamos com input()
    # Para rodar sem interação, troque por: houve_atraso = "s"
    houve_atraso = input("  ⏰ A devolução está atrasada? (s/n): ").strip().lower()
    if houve_atraso == "s":
        print("  📋 Multa aplicada! Por favor, dirija-se à recepção.")
    else:
        print("  👍 Devolução dentro do prazo. Sem multa!")


# ============================================================
# 🔎 ESTADO FINAL — confira o resultado
# ============================================================
print("\n📖 Catálogo após operações:")
for livro in catalogo:
    status = "✅" if livro["disponivel"] else "❌"
    print(f"  {status} {livro['titulo']}")

print(f"\n📋 Empréstimos ativos: {emprestimos}")