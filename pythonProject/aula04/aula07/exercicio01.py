e=0
qtd = int(input("Informe quantas vezes quer multiplicar: "))
for i in range(1, qtd+1):
    e = e + (2 ** i)
print(f"O valor de e = {e}")