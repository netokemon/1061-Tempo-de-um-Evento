dia1 = input().split(" ")
valorDia1 = int(dia1[1])

horario1 = input().split(" : ")
horaDia1 = int(horario1[0])
minutoDia1 = int(horario1[1])
segundoDia1 = int(horario1[2])

dia2 = input().split(" ")
valorDia2 = int(dia2[1])

horario2 = input().split(" : ")
horaDia2 = int(horario2[0])
minutoDia2 = int(horario2[1])
segundoDia2 = int(horario2[2])

horasLiquidas = (valorDia2-valorDia1)*24 - horaDia1+horaDia2 + (minutoDia1+minutoDia2)/60 + (segundoDia1+segundoDia2)/3600

diasTotais = horasLiquidas // 24

print(diasTotais)
#print("{} dia(s)\n{} hora(s)\n{} minuto(s)\n{} segundo(s)".format(valorDia2-valorDia1, horaTotal, 0, 0))
