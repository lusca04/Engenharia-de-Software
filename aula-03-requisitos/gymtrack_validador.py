import time

print("===================================")
print("   GymTrack - Controle de Treino")
print("===================================")

# Dados do treino
exercicio = "Supino Reto"
peso = 80
repeticoes = 10

# Validar nome do exercício
if exercicio != "":
    print("Nome do exercício válido")
else:
    print("Erro: exercício vazio")

# Validar peso
if peso >= 1 and peso <= 300:
    print("Peso válido")
else:
    print("Peso inválido")

# Validar repetições
if repeticoes >= 1 and repeticoes <= 50:
    print("Repetições válidas")
else:
    print("Quantidade de repetições inválida")

print("-----------------------------------")

# Verificar registro
inicio = time.time()

# Simulação de cadastro
time.sleep(0.05)

print("Treino registrado")
print(exercicio, "-", peso, "kg x", repeticoes, "repeticoes")

fim = time.time()

tempo = (fim - inicio) * 1000

if tempo < 200:
    print("Tempo de resposta OK")
    print(f"{tempo:.2f} ms")
else:
    print("Sistema demorou muito")