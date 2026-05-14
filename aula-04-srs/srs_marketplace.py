# ============================================================
# 🚀 SRS em Python — FIAP Marketplace
# Aula 04 — Engenharia de Software · FIAP
# Partes 1, 2 e 3 — Solução Completa
# ============================================================

from dataclasses import dataclass, field
from typing import List
from enum import Enum
import re


# MODELOS DE DADOS (do código original da aula)

class Prioridade(Enum):
    ALTA = "Alta"
    MEDIA = "Média"
    BAIXA = "Baixa"


@dataclass
class RequisitoFuncional:
    id: str
    nome: str
    descricao: str
    prioridade: Prioridade
    ator: str
    pre_condicao: str
    pos_condicao: str


@dataclass
class RequisitoNaoFuncional:
    id: str
    categoria: str  # Desempenho, Segurança, Usabilidade...
    descricao: str
    criterio_aceitacao: str


@dataclass
class SRS:
    projeto: str
    versao: str
    descricao: str
    requisitos_funcionais: List[RequisitoFuncional] = field(default_factory=list)
    requisitos_nao_funcionais: List[RequisitoNaoFuncional] = field(default_factory=list)

    def adicionar_rf(self, req: RequisitoFuncional):
        self.requisitos_funcionais.append(req)
        print(f"✅ RF '{req.id}' adicionado!")

    def adicionar_rnf(self, req: RequisitoNaoFuncional):
        self.requisitos_nao_funcionais.append(req)
        print(f"✅ RNF '{req.id}' adicionado!")

    def relatorio(self):
        print(f"\n{'='*50}")
        print(f"📋 SRS — {self.projeto} v{self.versao}")
        print(f"{'='*50}")
        print(f"📝 {self.descricao}\n")

        print(f"🔧 REQUISITOS FUNCIONAIS ({len(self.requisitos_funcionais)})")
        for rf in self.requisitos_funcionais:
            print(f"  [{rf.id}] {rf.nome} — Prioridade: {rf.prioridade.value}")
            print(f"       Ator: {rf.ator}")
            print(f"       📌 {rf.descricao}\n")

        print(f"⚡ REQUISITOS NÃO-FUNCIONAIS ({len(self.requisitos_nao_funcionais)})")
        for rnf in self.requisitos_nao_funcionais:
            print(f"  [{rnf.id}] {rnf.categoria}")
            print(f"       📌 {rnf.descricao}")
            print(f"       ✔️  Critério: {rnf.criterio_aceitacao}\n")


# PARTE 2 — Função de Validação de Requisitos

def validar_requisito(rf: RequisitoFuncional) -> dict:
    """
    Valida se um requisito funcional segue as boas práticas de engenharia.

    Verificações realizadas:
      1. Descrição com mais de 20 caracteres (evitar requisitos vagos)
      2. Pré-condição definida e não vazia
      3. Critério mensurável: presença de número na descrição

    Retorna um dict com chaves:
      - 'descricao_adequada'   : bool
      - 'pre_condicao_definida': bool
      - 'criterio_mensuravel'  : bool
      - 'valido'               : bool  (True somente se todos passarem)
      - 'avisos'               : list[str] com mensagens explicativas
    """
    resultados = {}
    avisos = []

    # 1. Descrição com mais de 20 caracteres
    descricao_adequada = len(rf.descricao) > 20
    resultados["descricao_adequada"] = descricao_adequada
    if not descricao_adequada:
        avisos.append(
            f"⚠️  Descrição muito curta ({len(rf.descricao)} chars). "
            "Use mais de 20 caracteres para evitar requisitos vagos."
        )

    # 2. Pré-condição não vazia (strip para rejeitar strings só com espaços)
    pre_condicao_definida = rf.pre_condicao.strip() != ""
    resultados["pre_condicao_definida"] = pre_condicao_definida
    if not pre_condicao_definida:
        avisos.append("⚠️  Pré-condição não definida. Toda funcionalidade deve ter um ponto de entrada claro.")

    # 3. Critério mensurável: ao menos um dígito na descrição
    #    (ex.: "atualizada a cada 3 segundos", "mínimo de 8 caracteres")
    criterio_mensuravel = any(char.isdigit() for char in rf.descricao)
    resultados["criterio_mensuravel"] = criterio_mensuravel
    if not criterio_mensuravel:
        avisos.append(
            "⚠️  Nenhum critério mensurável encontrado na descrição. "
            "Inclua valores numéricos (tempo, tamanho, quantidade, etc.)."
        )

    # Resultado final: válido apenas se todas as três checagens passaram
    resultados["valido"] = descricao_adequada and pre_condicao_definida and criterio_mensuravel
    resultados["avisos"] = avisos

    return resultados


def exibir_validacao(rf: RequisitoFuncional):
    """Exibe o resultado da validação de forma formatada."""
    resultado = validar_requisito(rf)
    status = "✅ VÁLIDO" if resultado["valido"] else "❌ INVÁLIDO"

    print(f"\n  [{rf.id}] {rf.nome} → {status}")
    print(f"       Descrição adequada  : {'✅' if resultado['descricao_adequada']    else '❌'}")
    print(f"       Pré-condição existe : {'✅' if resultado['pre_condicao_definida'] else '❌'}")
    print(f"       Critério mensurável : {'✅' if resultado['criterio_mensuravel']   else '❌'}")
    for aviso in resultado["avisos"]:
        print(f"       {aviso}")

# PARTE 3 — Exportação para Markdown

def exportar_markdown(srs: SRS) -> str:
    """
    Gera a documentação SRS completa em formato Markdown,
    pronto para ser colado no Confluence, Notion, GitHub Wiki, etc.

    Retorna a string com o conteúdo Markdown.
    """
    linhas = []

    # Cabeçalho
    linhas.append(f"# 📋 SRS — {srs.projeto}")
    linhas.append(f"\n**Versão:** {srs.versao}  ")
    linhas.append(f"**Descrição:** {srs.descricao}")
    linhas.append("\n---\n")

    # Sumário
    linhas.append("## 📑 Sumário\n")
    linhas.append("1. [Requisitos Funcionais](#requisitos-funcionais)")
    linhas.append("2. [Requisitos Não-Funcionais](#requisitos-não-funcionais)")
    linhas.append("\n---\n")

    # Requisitos Funcionais
    linhas.append(f"## 🔧 Requisitos Funcionais ({len(srs.requisitos_funcionais)})\n")

    for rf in srs.requisitos_funcionais:
        linhas.append(f"### {rf.id} — {rf.nome}\n")
        linhas.append(f"| Campo          | Detalhe |")
        linhas.append(f"|----------------|---------|")
        linhas.append(f"| **Prioridade** | {rf.prioridade.value} |")
        linhas.append(f"| **Ator**       | {rf.ator} |")
        linhas.append(f"| **Descrição**  | {rf.descricao} |")
        linhas.append(f"| **Pré-condição** | {rf.pre_condicao} |")
        linhas.append(f"| **Pós-condição** | {rf.pos_condicao} |")
        linhas.append("")

    linhas.append("---\n")

    # Requisitos Não-Funcionais
    linhas.append(f"## ⚡ Requisitos Não-Funcionais ({len(srs.requisitos_nao_funcionais)})\n")
    linhas.append("| ID | Categoria | Descrição | Critério de Aceitação |")
    linhas.append("|----|-----------|-----------|----------------------|")

    for rnf in srs.requisitos_nao_funcionais:
        linhas.append(f"| **{rnf.id}** | {rnf.categoria} | {rnf.descricao} | {rnf.criterio_aceitacao} |")

    linhas.append("\n---\n")
    linhas.append("*Documento gerado automaticamente pelo módulo SRS · FIAP Marketplace*")

    return "\n".join(linhas)

# INSTÂNCIA DO SRS — FIAP MARKETPLACE

srs = SRS(
    projeto="FIAP Marketplace",
    versao="1.0",
    descricao=(
        "Plataforma de e-commerce multi-vendedor com cadastro de produtos, "
        "busca, checkout e avaliação de vendedores."
    )
)

# ---- PARTE 1: Requisitos Funcionais ----

srs.adicionar_rf(RequisitoFuncional(
    id="RF-001",
    nome="Cadastro de Produto",
    descricao=(
        "O vendedor deve poder cadastrar um produto informando nome (mínimo 3 "
        "caracteres), descrição, preço e pelo menos 1 foto. "
        "O sistema valida todos os campos antes de salvar."
    ),
    prioridade=Prioridade.ALTA,
    ator="Vendedor",
    pre_condicao="Vendedor autenticado e com cadastro aprovado na plataforma",
    pos_condicao="Produto salvo no catálogo e disponível para busca em até 30 segundos"
))

srs.adicionar_rf(RequisitoFuncional(
    id="RF-002",
    nome="Busca por Categoria",
    descricao=(
        "O cliente pode filtrar produtos por categoria, faixa de preço e avaliação "
        "mínima (1 a 5 estrelas). Os resultados são paginados com até 20 itens por "
        "página e ordenados por relevância por padrão."
    ),
    prioridade=Prioridade.ALTA,
    ator="Cliente",
    pre_condicao="Ao menos 1 produto cadastrado e indexado no catálogo",
    pos_condicao="Lista de produtos filtrada exibida em menos de 2 segundos"
))

srs.adicionar_rf(RequisitoFuncional(
    id="RF-003",
    nome="Checkout e Pagamento",
    descricao=(
        "O cliente pode finalizar a compra escolhendo entre cartão de crédito "
        "(até 12 parcelas), PIX ou boleto bancário. "
        "O pedido é confirmado somente após aprovação do pagamento pela gateway."
    ),
    prioridade=Prioridade.ALTA,
    ator="Cliente",
    pre_condicao="Carrinho com ao menos 1 item e cliente autenticado",
    pos_condicao="Pedido criado com status 'Aguardando envio' e e-mail de confirmação enviado em 1 minuto"
))

srs.adicionar_rf(RequisitoFuncional(
    id="RF-004",
    nome="Avaliação do Vendedor",
    descricao=(
        "Após receber o pedido, o cliente pode avaliar o vendedor com nota de 1 a 5 "
        "estrelas e comentário de até 500 caracteres. "
        "Cada cliente pode avaliar o mesmo vendedor no máximo 1 vez por pedido."
    ),
    prioridade=Prioridade.MEDIA,
    ator="Cliente",
    pre_condicao="Pedido com status 'Entregue' e prazo máximo de 30 dias após entrega",
    pos_condicao="Avaliação publicada no perfil do vendedor e média recalculada imediatamente"
))

# ---- PARTE 1: Requisitos Não-Funcionais ----

srs.adicionar_rnf(RequisitoNaoFuncional(
    id="RNF-001",
    categoria="Disponibilidade",
    descricao=(
        "A plataforma deve estar disponível 99,9% do tempo (downtime máximo de "
        "8,7 horas/ano), exceto janelas de manutenção programadas com 48 horas "
        "de antecedência."
    ),
    criterio_aceitacao=(
        "Monitoramento via UptimeRobot com alertas em < 1 minuto. "
        "Relatório mensal de SLA disponibilizado aos stakeholders."
    )
))

srs.adicionar_rnf(RequisitoNaoFuncional(
    id="RNF-002",
    categoria="Desempenho",
    descricao=(
        "O tempo de resposta da busca deve ser inferior a 2 segundos para "
        "consultas com até 10.000 produtos indexados, suportando 5.000 "
        "usuários simultâneos."
    ),
    criterio_aceitacao=(
        "Teste de carga com k6: 5.000 usuários virtuais, p95 < 2s, "
        "taxa de erro < 0,1%."
    )
))

srs.adicionar_rnf(RequisitoNaoFuncional(
    id="RNF-003",
    categoria="Conformidade com LGPD",
    descricao=(
        "Todos os dados pessoais dos clientes (nome, CPF, endereço, histórico de "
        "compras) devem ser coletados com consentimento explícito, armazenados "
        "com criptografia AES-256 e excluídos em até 30 dias após solicitação."
    ),
    criterio_aceitacao=(
        "Auditoria semestral por DPO certificado; relatório de impacto (RIPD) "
        "aprovado antes do lançamento; funcionalidade 'Excluir minha conta' "
        "testada e documentada."
    )
))

# EXIBIÇÃO DO RELATÓRIO

srs.relatorio()

# PARTE 2 — Validação dos Requisitos Funcionais

print(f"\n{'='*50}")
print("🔍 VALIDAÇÃO DOS REQUISITOS FUNCIONAIS")
print(f"{'='*50}")

for rf in srs.requisitos_funcionais:
    exibir_validacao(rf)

# Demonstração com um requisito propositalmente inválido
print("\n--- Demonstração com requisito inválido ---")
rf_invalido = RequisitoFuncional(
    id="RF-XXX",
    nome="Login",
    descricao="Fazer login",       # < 20 chars, sem número
    prioridade=Prioridade.ALTA,
    ator="Cliente",
    pre_condicao="",               # pré-condição vazia
    pos_condicao="Usuário logado"
)
exibir_validacao(rf_invalido)

# PARTE 3 — Exportação para Markdown

print(f"\n{'='*50}")
print("📄 EXPORTANDO PARA MARKDOWN")
print(f"{'='*50}")

markdown = exportar_markdown(srs)

# Salva em arquivo
with open("srs_fiap_marketplace.md", "w", encoding="utf-8") as f:
    f.write(markdown)

print("\n✅ Arquivo 'srs_fiap_marketplace.md' gerado com sucesso!")
print("\n--- Prévia das primeiras linhas ---\n")
print("\n".join(markdown.split("\n")[:20]))
print("...")