# ============================================================
# 🚀 Cadastro de Usuário — Diagrama de Atividades
# ============================================================
import re

def cadastro_usuario(email: str, senha: str, email_ja_existe: bool, confirmou_email: bool) -> str:
    """
    Implementação baseada no diagrama de atividades (estilo iFood).

    Fluxo:
    1. Validar formato do e-mail
    2. Verificar se e-mail já está cadastrado
    3. Criar conta
    4. Enviar e-mail de confirmação
    5. Aguardar confirmação do usuário
    6. Liberar acesso OU expirar cadastro
    """

    # ── Passo 1: Validar formato do e-mail ──────────────────
    padrao_email = r"^[\w\.-]+@[\w\.-]+\.\w{2,}$"
    if not re.match(padrao_email, email):
        return "E-mail inválido. Verifique o formato (ex: joao@email.com)."

    # ── Passo 2: Verificar se e-mail já está cadastrado ─────
    if email_ja_existe:
        return "E-mail já cadastrado. Faça login ou recupere sua senha."

    # ── Passo 3: Criar conta ────────────────────────────────
    print(f"Conta criada para {email} (aguardando confirmação)...")

    # ── Passo 4: Enviar e-mail de confirmação ───────────────
    print(f"E-mail de confirmação enviado para {email}.")

    # ── Passo 5 + 6: Confirmação → liberar ou expirar ───────
    if not confirmou_email:
        return "Cadastro expirado. O link de confirmação não foi utilizado."

    return f"Cadastro concluído! Bem-vindo(a), {email}."



# Testes (não apague!)
print(cadastro_usuario("joao@email.com", "senha123", False, True))  
print(cadastro_usuario("email-invalido", "senha123", False, True))   
print(cadastro_usuario("joao@email.com", "senha123", True,  True))  
