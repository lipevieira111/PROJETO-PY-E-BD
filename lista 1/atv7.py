# Inicializar o contador de respostas positivas
respostas_positivas = 0

# Fazer as 5 perguntas e contar as respostas positivas
print("Responda 'sim' ou 'não' para as seguintes perguntas:")
if input("Telefonou para a vítima? ").lower() == "sim":
    respostas_positivas += 1
if input("Esteve no local do crime? ").lower() == "sim":
    respostas_positivas += 1
if input("Mora perto da vítima? ").lower() == "sim":
    respostas_positivas += 1
if input("Devia para a vítima? ").lower() == "sim":
    respostas_positivas += 1
if input("Já trabalhou com a vítima? ").lower() == "sim":
    respostas_positivas += 1

# Determinar a classificação
if respostas_positivas == 2:
    print("Classificação: Suspeita")
elif 3 <= respostas_positivas <= 4:
    print("Classificação: Cúmplice")
elif respostas_positivas == 5:
    print("Classificação: Assassino")
else:
    print("Classificação: Inocente")