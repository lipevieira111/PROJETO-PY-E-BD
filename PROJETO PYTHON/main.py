from usuario import Usuario
from login import login
from cadastrar_pousada import cadastrar_pousada
from buscar_por_cidade import buscar_por_cidade
from buscar_por_preco import buscar_por_preco
from alugar_quarto import alugar_quarto

MAX_POUSADAS = 100

def main():
    usuarios = [Usuario("filipe", "0101"), Usuario("julio", "1010")]
    pousadas = []
    indice_usuario_logado = -1

    while True:
        print("=== Gerenciador de Pousadas ===")
        print("1. Login")
        print("2. Cadastro de Pousada")
        print("3. Buscar pousada por Cidade")
        print("4. Buscar pousada por Preço")
        print("5. Alugar quarto")
        print("0. Sair")
        opcao = input("Opção: ")

        if opcao == "1":
            if indice_usuario_logado != -1:
                print("Usuário já está logado.")
            else:
                indice_usuario_logado = login(usuarios)
        elif opcao == "2":
            if indice_usuario_logado == -1:
                print("Nenhum usuário logado.")
            else:
                cadastrar_pousada(pousadas)
        elif opcao == "3":
            buscar_por_cidade(pousadas)
        elif opcao == "4":
            buscar_por_preco(pousadas)
        elif opcao == "5":
            if indice_usuario_logado == -1:
                print("Nenhum usuário logado.")
            else:
                alugar_quarto(pousadas)
        elif opcao == "0":
            print("Saindo...")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()
