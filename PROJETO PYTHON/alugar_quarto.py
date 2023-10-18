def alugar_quarto(pousadas):
    print("=== Alugar Quarto ===")
    cidade = input("Cidade: ")
    try:
        preco = float(input("Preço máximo: "))
        dias = int(input("Quantos dias irá ficar: "))
    except ValueError:
        print("Erro: Valor inválido inserido.")
        return

    print("=== Resultados da busca ===")
    encontrou = False

    for pousada in pousadas:
        if (
            pousada.cidade == cidade
            and pousada.diaria <= preco
            and pousada.quartos_disponiveis > 0
        ):
            print(f"Pousada: {pousada.nome}")
            print(f"Diária: {pousada.diaria:.2f}")
            print("==========================")

            # Atualiza o número de quartos disponíveis
            pousada.quartos_disponiveis -= 1

            # Calcula o valor total do aluguel
            valor_total = pousada.diaria * dias
            print(f"Valor total do aluguel: {valor_total:.2f}")

            encontrou = True
            break

    if not encontrou:
        print("Nenhuma pousada encontrada com os critérios informados.")
