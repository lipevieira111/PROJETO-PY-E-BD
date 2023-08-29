while True:
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    
    resultado = num1 + num2
    print(f"O resultado da adição é: {resultado}")
    
    continuar = input("Deseja fazer outra conta de adição? (s/n): ")
    if continuar.lower() != 's':
        print("obrigado por participar!!!")
        break
    
