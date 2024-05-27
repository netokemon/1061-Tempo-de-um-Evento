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

diaFinal = valorDia2 - valorDia1

horaFinal = horaDia2 - horaDia1

if horaFinal < 0:
    diaFinal -= 1
    horaFinal += 24

minutoFinal = minutoDia2 - minutoDia1

if minutoFinal < 0:
    horaFinal -= 1
    minutoFinal += 60

segundoFinal = segundoDia2 - segundoDia1

if segundoFinal < 0:
    minutoFinal -= 1
    segundoFinal += 60

if diaFinal < 0:
    diaFinal == 0
print("{} dia(s)\n{} hora(s)\n{} minuto(s)\n{} segundo(s)".format(diaFinal, horaFinal, minutoFinal, segundoFinal))
