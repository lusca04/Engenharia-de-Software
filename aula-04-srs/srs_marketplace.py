from enum import Enum


# Prioridade
class Prioridade(Enum):
    ALTA = "Alta"
    MEDIA = "Média"
    BAIXA = "Baixa"


# Requisito funcional
class RequisitoFuncional:

    def __init__(self, id, nome, descricao, prioridade):
        self.id = id
        self.nome = nome
        self.descricao = descricao
        self.prioridade = prioridade


# Requisito não funcional
class RequisitoNaoFuncional:

    def __init__(self, id, categoria, descricao):
        self.id = id
        self.categoria = categoria
        self.descricao = descricao


# SRS
class SRS:

    def __init__(self, projeto):
        self.projeto = projeto
        self.rf = []
        self.rnf = []

    # requisito funcional
    def adicionar_rf(self, requisito):
        self.rf.append(requisito)

    #r equisito nao funcional
    def adicionar_rnf(self, requisito):
        self.rnf.append(requisito)

    # relatorio
    def relatorio(self):

        print("PROJETO:", self.projeto)

        print("\nREQUISITOS FUNCIONAIS")

        for item in self.rf:
            print(item.id, "-", item.nome)
            print("Descrição:", item.descricao)
            print("Prioridade:", item.prioridade.value)
            print()

        print("REQUISITOS NÃO FUNCIONAIS")

        for item in self.rnf:
            print(item.id, "-", item.categoria)
            print("Descrição:", item.descricao)
            print()


# sistema
srs = SRS("App Delivery")

# RF
rf1 = RequisitoFuncional(
    "RF-01",
    "Login",
    "Usuário deve fazer login",
    Prioridade.ALTA
)

rf2 = RequisitoFuncional(
    "RF-02",
    "Rastreamento",
    "Mostrar entregador no mapa",
    Prioridade.MEDIA
)

rnf1 = RequisitoNaoFuncional(
    "RNF-01",
    "Desempenho",
    "Sistema deve ser rápido"
)

srs.adicionar_rf(rf1)
srs.adicionar_rf(rf2)
srs.adicionar_rnf(rnf1)

srs.relatorio()