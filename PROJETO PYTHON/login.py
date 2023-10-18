def login(usuarios):
    username = input("Username: ")
    password = input("Password: ")

    for i, user in enumerate(usuarios):
        if user.username == username and user.password == password:
            print("Login realizado com sucesso!")
            return i  # Retorna o índice do usuário logado

    print("Erro: Usuário ou senha incorretos.")
    return -1
