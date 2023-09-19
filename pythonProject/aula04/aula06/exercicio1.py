num = int(input("Digite o número que deseja saber se são divisíveis por 3 e 5: "))
if (num % 3 == 0) and (num % 5 == 0):
    print("O número", num, " é divisível por 3 e 5: ")
else:
    print("O número", num, " não é divisível por 3 e por 5: ")