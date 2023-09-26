soma = 0
qtde = int(input("Com quantas idades deseja calcular a média? "))
for i in range(1, qtde+1):
    n = int(input(f"Entre com a {i}ª idade: "))
    soma = soma + n
media = soma / qtde
print(f"A média das idades é {media:5.2f}")