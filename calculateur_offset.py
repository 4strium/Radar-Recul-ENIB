vcc = 15

offset_voulu = float(input("Saisissez l'offset recherché en Volt :\n"))

r1 = vcc - offset_voulu

print("Positionnez une résistance de",r1,"(k)ohms en série avec une résistance de",offset_voulu,"(k)ohms, puis prenez la tension entre les deux résistances.")
