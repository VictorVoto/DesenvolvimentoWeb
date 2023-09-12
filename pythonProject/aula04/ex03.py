anoNasc = int(input("Em que ano você nasceu: "))
anoAtual = int(input("Em que ano estamos: "))
respAno = anoAtual - anoNasc
respMes = respAno * 12
respDias = respAno * 365
respSema = respAno * 53
print("a) Idade em anos: ", respAno, "anos")
print("b) Idade em meses: ", respMes, "meses")
print("c) Idade em dias: ", respDias, "dias")
print("d) Idade em semanas: ", respSema, "semanas")