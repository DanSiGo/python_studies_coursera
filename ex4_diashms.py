segundos_total = input("Por favor, entre com o número de segundos que deseja converter: ")

segs_int = int(segundos_total)

dias = segs_int // 86400
segs_dias = segs_int % 86400

horas = segs_dias // 3600
segs_minutos = segs_dias % 3600

minutos = segs_minutos // 60
segs_restantes = segs_minutos % 60

segundos = segs_restantes

print(dias, "dias,", horas, "horas,", minutos, "minutos e", segundos, "segundos.")