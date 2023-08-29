# Solicitar uma letra ao usuário
letra = input("Digite uma letra: ")

# Converter para letra minúscula para facilitar a verificação
letra = letra.lower()

# Verificar se é uma letra do alfabeto
if letra.isalpha() and len(letra) == 1:
    if letra in 'aeiou':
        print("É uma vogal.")
    else:
        print("É uma consoante.")
else:
    print("Por favor, digite uma única letra do alfabeto.")