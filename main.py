def menu_principal():
    print("calculadora giovanna")
    print("3. sair")

    opcao = input("digite o que deseja: ")
    return opcao

def sair():
    print("encerrar programa")

escolha = menu_principal()

if escolha == 3:
    sair()
