def cadastrar_pousada(pousadas):
    print("=== Cadastro de Pousada ===")
    try:
        nome = input("Nome: ")
        diaria = float(input("Diária: "))
        cidade = input("Cidade: ")
        quartos_disponiveis = int(input("Quartos disponíveis: "))
    except ValueError:
        print("Erro: Valor inválido inserido.")
        return

    pousada = Pousada(nome, diaria, cidade, quartos_disponiveis)
    pousadas.append(pousada)
    print("Pousada cadastrada com sucesso!")
