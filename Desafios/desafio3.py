# Solicita ao usuário a quantidade de números no conjunto (N)
N = int(input("Digite a quantidade de números no conjunto: "))

# Inicializa variáveis para armazenar o menor valor, o maior valor e a soma
menor_valor = 1001  # Inicializa com um valor maior do que o máximo permitido
maior_valor = -1     # Inicializa com um valor menor do que o mínimo permitido
soma_valores = 0

# Solicita ao usuário que insira os números e realiza os cálculos
for i in range(N):
    numero = float(input(f"Digite o {i + 1}º número (entre 0 e 1000): "))
    
    # Verifica se o número está dentro do intervalo permitido
    if 0 <= numero <= 1000:
        # Verifica se o número é menor ou maior que os atuais valores armazenados
        if numero < menor_valor:
            menor_valor = numero
        if numero > maior_valor:
            maior_valor = numero
        
        # Soma o valor ao acumulador
        soma_valores += numero
    else:
        print("Número fora do intervalo permitido (0 a 1000). Tente novamente.")

# Imprime os resultados
print(f"Menor valor: {menor_valor}")
print(f"Maior valor: {maior_valor}")
print(f"Soma dos valores: {soma_valores}")