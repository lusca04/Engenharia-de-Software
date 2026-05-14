# ============================================================
# 🏦 Sistema de Transferência — Diagrama de Sequência
# Cliente → AppNubank → ServidorNubank → BancoDeDados
# ============================================================

#Célula 1 — BancoDeDados (Participante 4)
class BancoDeDados:
    def __init__(self):
        # Repositório de saldos: { user_id: saldo }
        self.saldos = {
            "user_123": 500.0
        }

    def verificar_saldo(self, user_id: str) -> float:
        # .get evita KeyError: retorna 0.0 se usuário não existe
        return self.saldos.get(user_id, 0.0)

    def debitar(self, user_id: str, valor: float) -> bool:
        saldo_atual = self.verificar_saldo(user_id)

        if saldo_atual >= valor:
            self.saldos[user_id] = saldo_atual - valor
            return True         # débito realizado

        return False            # saldo insuficiente

#Célula 2 — ServidorNubank (Participante 3)
class ServidorNubank:
    def __init__(self):
        self.banco = BancoDeDados()   # mensagem 3 do diagrama: acessa o banco

    def processar_transferencia(self, user_id: str, valor: float) -> dict:
        """
        Fragmento [alt] do diagrama de sequência:
          [alt] saldo suficiente  → debita e retorna aprovado
          [else]                  → retorna recusado
        """
        # Mensagem 3: processar pagamento → consulta banco
        sucesso = self.banco.debitar(user_id, valor)

        if sucesso:
            # Mensagem 4: pagamento aprovado
            saldo_restante = self.banco.verificar_saldo(user_id)
            return {"status": "aprovado", "saldo_restante": saldo_restante}
        else:
            # Fragmento [else]: recusa com motivo
            return {"status": "recusado", "motivo": "saldo insuficiente"}

#Célula 3 — AppNubank (Participante 2)
class AppNubank:
    def __init__(self):
        self.servidor = ServidorNubank()   # app conhece o servidor

    def transferir(self, user_id: str, valor: float):
        # Mensagem 1+2 do diagrama: cliente confirma pedido no app
        print(f"[APP] Iniciando transferência de R$ {valor:.2f}...")

        # Mensagem 3: app envia para o servidor processar
        resultado = self.servidor.processar_transferencia(user_id, valor)

        # Mensagens 6+7: servidor responde → app notifica o cliente
        if resultado["status"] == "aprovado":
            print(f"[APP] ✅ Transferência aprovada! "
                  f"Saldo restante: R$ {resultado['saldo_restante']:.2f}")
        else:
            print(f"[APP] ❌ Transferência recusada: {resultado['motivo']}")


#Célula 4 — Testes (não altere, apenas execute)
# Rode esta célula só depois de completar as anteriores!
app = AppNubank()
print("=== Teste 1: Transferência dentro do saldo ===")

app.transferir("user_123", 200.0)   # Esperado: ✅ aprovado
print("\n=== Teste 2: Transferência acima do saldo ===")

app.transferir("user_123", 500.0)   # Esperado: ❌ recusado
print("\n=== Teste 3: Múltiplas transferências ===")

app.transferir("user_123", 100.0)   # Esperado: ✅ aprovado (saldo agora 200)
app.transferir("user_123", 250.0)   # Esperado: ❌ recusado (saldo insuficiente)