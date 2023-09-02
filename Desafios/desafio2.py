# Solicita ao usuário a quantidade de números no conjunto (N)
N = int(input("Digite a quantidade de números no conjunto: "))

# Inicializa variáveis para armazenar o menor valor, o maior valor e a soma
menor_valor = float('inf')  # Inicializa com infinito para garantir que qualquer número digitado seja menor
maior_valor = float('-inf')  # Inicializa com negativo infinito para garantir que qualquer número digitado seja maior
soma_valores = 0

# Solicita ao usuário que insira os números e realiza os cálculos
for i in range(N):
    numero = float(input(f"Digite o {i + 1}º número: "))
    
    # Verifica se o número é menor ou maior que os atuais valores armazenados
    if numero < menor_valor:
        menor_valor = numero
    if numero > maior_valor:
        maior_valor = numero
    
    # Soma o valor ao acumulador
    soma_valores += numero

# Imprime os resultados
print(f"Menor valor: {menor_valor}")
print(f"Maior valor: {maior_valor}")
print(f"Soma dos valores: {soma_valores}")
