def menu_principal():
    print("CONVERSOR DE MEDIDAS")
    print("Conversor de Temperatura")
    print("3. sair")

    opcao = input("digite o que deseja: ")
    return opcao

def sair():
    print("encerrar programa")

escolha = menu_principal()

if escolha == 3:
    sair()
