def buscar_por_preco(pousadas):
    try:
        preco = float(input("Digite o preço máximo: "))
    except ValueError:
        print("Erro: Valor inválido inserido.")
        return

    print("=== Resultados da busca ===")
    encontrou = False

    for pousada in pousadas:
        if pousada.diaria <= preco:
            print(f"Pousada: {pousada.nome}")
            print(f"Diária: {pousada.diaria:.2f}")
            print(f"Quartos disponíveis: {pousada.quartos_disponiveis}")
            print("==========================")
            encontrou = True

    if not encontrou:
        print("Nenhuma pousada encontrada com os critérios informados.")
