a = 0
p = 0
maiorImc = 0
menorImc = 0
for i in range(1,6):
    altura = float(input(f"informe a altura da {i}ª pessoa: "))
    peso = float(input(f"informe o peso da {i}ª pessoa: "))
    a = a + altura
    p = p + peso
    alturaMedia = a / 5
    pesoMedio = p / 5
    imc = peso / (altura ** 2)
    if i == 1:
        maiorImc = imc
        menorImc = imc
    if imc > maiorImc:
        maiorImc = imc
    if imc < menorImc:
        menorImc = imc
        
print(f"A altura média é: {alturaMedia:.2f}")
print(f"O peso médio é: {pesoMedio:.2f}")
print(f"O maior IMC é: {maiorImc:.2f}")
print(f"O menor IMC é: {menorImc:.2f}")