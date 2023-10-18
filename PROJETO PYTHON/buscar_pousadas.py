def buscar_pousadas(pousadas, filtro):
    print("=== Resultados da busca ===")
    encontrou = False

    for pousada in pousadas:
        if filtro(pousada):
            print(f"Pousada: {pousada.nome}")
            print(f"Diária: {pousada.diaria:.2f}")
            print(f"Quartos disponíveis: {pousada.quartos_disponiveis}")
            print("==========================")
            encontrou = True

    if not encontrou:
        print("Nenhuma pousada encontrada com os critérios informados.")
