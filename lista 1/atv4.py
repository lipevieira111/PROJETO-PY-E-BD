# Solicitar as duas notas ao usuário
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

# Calcular a média
media = (nota1 + nota2) / 2

# Verificar as condições e apresentar a mensagem
if media == 10:
    print("Aprovado com Distinção")
elif media >= 7:
    print("Aprovado")
else:
    print("Reprovado")