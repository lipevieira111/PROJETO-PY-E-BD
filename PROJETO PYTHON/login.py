def login(usuarios, indice_usuario_logado):
    if indice_usuario_logado != -1:
        print("Você já está logado como usuário", usuarios[indice_usuario_logado].username)
        opcao = input("Deseja deslogar? (S/N): ").upper()
        if opcao == "S":
            print("Logout realizado com sucesso!")
            return -1  # Retorna -1 para indicar que o usuário foi deslogado
        else:
            return indice_usuario_logado  # Retorna o mesmo índice de usuário logado
    else:
        username = input("Username: ")
        password = input("Password: ")

        for i, user in enumerate(usuarios):
            if user.username == username and user.password == password:
                print("Login realizado com sucesso!")
                return i  # Retorna o índice do usuário logado

        print("Erro: Usuário ou senha incorretos.")
        return -1
