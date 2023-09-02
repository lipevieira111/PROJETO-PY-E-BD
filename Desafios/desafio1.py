# Inicialize os dois primeiros números da série
a, b = 0, 1

# Imprima o primeiro número da série
print(a)

# Gere a série de Fibonacci até que o valor seja maior que 500
while b <= 500:
    # Imprima o próximo número da série
    print(b)
    
    # Calcule o próximo número da série
    a, b = b, a + b