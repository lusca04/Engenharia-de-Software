from datetime import datetime


class ContaBancaria:
    def __init__(self, titular, banco, saldo=0):
        self.titular = titular
        self.banco = banco
        self.saldo = saldo

    def transferir(self, destino, valor):
        print("Transferindo...")
        # valida valor
        if valor <= 0:
            print("Valor inválido.")
            return

        # verifica saldo
        if self.saldo < valor:
            print(f"Saldo insuficiente. Saldo atual: R$ {self.saldo:.2f} da conta {self.titular}. Valor solicitado: R$ {valor:.2f}.")
            return

        # realiza transferência
        self.saldo -= valor
        print(f"Saldo Debitado da conta origem: R$ {self.saldo:.2f} da conta {self.titular}.")
        destino.saldo += valor
        print(f"Saldo Creditado na conta destino: R$ {destino.saldo:.2f} da conta {destino.titular}.")

        # comprovante
        print("\n" + "=" * 40)
        print("TRANSFERÊNCIA REALIZADA")
        print("=" * 40)

        print(f"De      : {self.titular}")
        print(f"Para    : {destino.titular}")
        print(f"Banco   : {self.banco} -> {destino.banco}")
        print(f"Valor   : R$ {valor:.2f}")
        print(f"Data    : {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")

        print("=" * 40)


# contas
conta_joao = ContaBancaria("João Silva", "Nubank", 1500)
conta_maria = ContaBancaria("Maria Souza", "Itaú", 200)

# transferência válida
conta_joao.transferir(conta_maria, 300)

print(f"\nSaldo João : R$ {conta_joao.saldo:.2f}")
print(f"Saldo Maria: R$ {conta_maria.saldo:.2f}")

# transferência inválida
conta_joao.transferir(conta_maria, 5000)