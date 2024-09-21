time = input("Introduce la hora en formato ##:##: ")
hours, minutes = time.split(":")
time_in_hours = float(hours) + float(minutes) / 60

if 7 <= time_in_hours <= 8:
    print("Es hora del desayuno")
elif 12 <= time_in_hours <= 13:
    print("Es hora del almuerzo")
elif 18 <= time_in_hours <= 19:
    print("Es hora de la cena")
