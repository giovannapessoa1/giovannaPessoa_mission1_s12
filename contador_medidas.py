class Conversor_medidas:
    def _init_(self):
        pass

    def centimetrosParaMetros(centimetros):
        return centimetros / 100

def metrosParaCentimetros(metros):
    return metros * 100
print("Conversor de Medidas")
print("1. Converter de centímetros para metros")
print("2. Converter de metros para centímetros")
while True:
     escolha = input("Escolha uma opção: ")
     if escolha == "1":
         centimetros = float(input("Digite o valor em centímetros: "))
         metros = CentimetrosParaMetros(centimetros)
         print(f"{centimetros} centímetros é igual a {metros} metros")
     elif escolha == "2":
            metros = float(input("Digite o valor em metros: "))
            centimetros = MetrosParaCentimetros(metros)
            print(f"{metros} metros é igual a {centimetros} centímetros")
     elif escolha=="sair":
            break
     else:
            print("Opção inválida. Por favor, tente novamente.")