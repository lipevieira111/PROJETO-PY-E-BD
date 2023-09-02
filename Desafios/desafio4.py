# Função para validar o nome
def validar_nome(nome):
    return len(nome) > 3

# Função para validar a idade
def validar_idade(idade):
    return 0 <= idade <= 150

# Função para validar o salário
def validar_salario(salario):
    return salario > 0

# Função para validar o sexo
def validar_sexo(sexo):
    return sexo in ('f', 'm')

# Função para validar o estado civil
def validar_estado_civil(estado_civil):
    return estado_civil in ('s', 'c', 'v', 'd')

# Solicitar as informações ao usuário
nome = input("Digite o nome: ")
idade = int(input("Digite a idade: "))
salario = float(input("Digite o salário: "))
sexo = input("Digite o sexo (f/m): ")
estado_civil = input("Digite o estado civil (s/c/v/d): ")

# Validar as informações
if (
    validar_nome(nome) and
    validar_idade(idade) and
    validar_salario(salario) and
    validar_sexo(sexo) and
    validar_estado_civil(estado_civil)
):
    print("Todas as informações são válidas.")
else:
    print("Alguma informação não é válida de acordo com os critérios especificados.")