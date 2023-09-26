while True:
    x = float(input("Entre com o valor da base: "))
    y = float(input("Entre com o valor da altura: "))
    if x > 0 and y > 0:
        break
    if x <= 0:
        print("A base tem que ser maior do que 0")
    if y <= 0:
        print("A altura tem que ser maior do que 0")
area = (x * y) / 2
print(f"A área do triangulo é = {area}")