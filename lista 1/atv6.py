# Solicitar o turno de estudo ao usuário
turno = input("Em que turno você estuda? (M-matutino / V-vespertino / N-noturno): ")

# Converter para letra maiúscula para facilitar a verificação
turno = turno.upper()

# Verificar o turno e imprimir a mensagem correspondente
if turno == "M":
    print("Bom Dia!")
elif turno == "V":
    print("Boa Tarde!")
elif turno == "N":
    print("Boa Noite!")
else:
    print("Valor Inválido!")