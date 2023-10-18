def buscar_por_cidade(pousadas):
    cidade = input("Digite a cidade: ")
    
    print("=== Resultados da busca ===")
    encontrou = False
    
    for pousada in pousadas:
        if pousada.cidade == cidade:
            print(f"Pousada: {pousada.nome}")
            print(f"Diária: {pousada.diaria:.2f}")
            print(f"Quartos disponíveis: {pousada.quartos_disponiveis}")
            print("==========================")
            encontrou = True
    
    if not encontrou:
        print("Nenhuma pousada encontrada na cidade informada.")
