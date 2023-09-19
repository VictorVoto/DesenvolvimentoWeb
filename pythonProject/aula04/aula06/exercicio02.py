valor = float(input("Informe o valor da compra: "))
if (valor <= 1000):
    result = valor * .9
    print(f"Sua compra de: R${valor:.2f} ficou: R${result:.2f} com o desconto de 10% aplicado")
else:
    if (valor > 1000 and valor <= 5000):
        result = valor * .8
        print(f"Sua compra de: R${valor:.2f} ficou: R${result:.2f} com o desconto de 20% aplicado")
    else: 
        if (valor > 5000):
            result = valor * .7
            print(f"Sua compra de: R${valor:.2f} ficou: R${result:.2f} com o desconto de 30% aplicado")