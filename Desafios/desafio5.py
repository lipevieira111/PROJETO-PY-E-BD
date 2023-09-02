# Função para verificar se um número é primo
def is_primo(numero):
    if numero <= 1:
        return False  # Números menores ou iguais a 1 não são primos
    elif numero <= 3:
        return True   # 2 e 3 são primos
    elif numero % 2 == 0 or numero % 3 == 0:
        return False  # Números divisíveis por 2 ou 3 não são primos

    # Verificar divisibilidade por outros números ímpares até a raiz quadrada do número
    i = 5
    while i * i <= numero:
        if numero % i == 0 or numero % (i + 2) == 0:
            return False
        i += 6

    return True

# Solicitar um número inteiro ao usuário
numero = int(input("Digite um número inteiro: "))

# Verificar se o número é primo e exibir o resultado
if is_primo(numero):
    print(f"{numero} é um número primo.")
else:
    print(f"{numero} não é um número primo.")