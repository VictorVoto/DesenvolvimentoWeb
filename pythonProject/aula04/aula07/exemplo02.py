soma = 0
for i in range(1, 11):
    idade = int(input(f"Informe a {i}º idade: "))
    soma = soma + idade
media = soma/10
print(f"A média é: {media}")