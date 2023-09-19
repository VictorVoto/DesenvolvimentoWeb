porta = .8 * 2.1
largura = int(input("Entre com o valor da Largura do aposento: "))
comprimento = int(input("Entre com o valor do Comprimento do aposento: "))
area = (((largura * 2.8) + (comprimento * 2.8)) * 2) - porta
print(f"{area:.2f}")
latas = area / 54
galao = area / 10.8
litro = area / 3

tipoLata = input("Informe qual tipo de lata quer (lata, galão ou litro): ")
if tipoLata == 'lata':
    if (latas % 2 != 0):
        print(f"Área para ser pintada: {area:.2f}")
        print(f"Quantidade de latas de 18 litros que serão usadas: {latas+1:.0f}")
    else:
        print(f"Área para ser pintada: {area:.2f}")
        print(f"Quantidade de latas de 18 litros que serão usadas: {latas:.2f}")

if tipoLata == 'galao':
    if (galao % 2 != 0):
        print(f"Área para ser pintada: {area:.2f}")
        print(f"Quantidade de latas de 18 litros que serão usadas: {galao+1:.0f}")
    else:
        print(f"Área para ser pintada: {area:.2f}")
        print(f"Quantidade de latas de 18 litros que serão usadas: {galao:.2f}")
    
if tipoLata == 'litro':
    if (litro % 2 != 0):
        print(f"Área para ser pintada: {area:.2f}")
        print(f"Quantidade de latas de 18 litros que serão usadas: {litro+1:.0f}")
    else:
        print(f"Área para ser pintada: {area:.2f}")
        print(f"Quantidade de latas de 18 litros que serão usadas: {litro:.2f}")
    


