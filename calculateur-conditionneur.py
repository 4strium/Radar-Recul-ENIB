valeurs_connues = {20:0.074,150:0.575}

distance_inp = int(input("Saisissez la distance de recul désirée (en cm) :\n"))

if 10 <= distance_inp <= 190 :
    tension_attendue = round((distance_inp * valeurs_connues[20])/20,3)
    tension_conditionneur = round((tension_attendue*(-4.7/1.77))+2.2,3)
    print("Pour une distance mesurée de",distance_inp,"cm :\nLa tension en sortie du capteur sera de",tension_attendue,"V\nLa tension en sortie du conditionneur sera de",tension_conditionneur,"V")
