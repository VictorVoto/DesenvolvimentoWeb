n = 0
par = 0
for i in range (2, 101, 2):
    print(f"\n{par}")
    par = par + i
    # par = print(f"O valor de par é = {par + i}")
    # i = i + 2
print(f"\nO valor final de par é: {par}")