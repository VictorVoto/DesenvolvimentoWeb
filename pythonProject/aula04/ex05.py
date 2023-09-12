salario = float(input("Informe seu salário: R$ "))
percentual = float(input("Informe a porcentagem de aumento que seu salário terá: "))
aumento = percentual / 100
valorAumento = aumento * salario
novoSalario = salario * (aumento + 1)
print(f"Valor aumento: {valorAumento:.2f}")
print(f"O valor do seu salário com o reajuste é de: {novoSalario:.2f}")