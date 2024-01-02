# zamisljeni broj = 82
# 41 -> unijeli ste manji broj od zamisljenog
# 80 -> unijeli ste manji broj od zamisljenog
# 95 -> unijeli ste veci broj od zamisljenog
# 82 -> CETITAMO, pogodili ste broj iz 4 pokusaja

#IMPORT DIO
import random


# DEKLARACIJA
zamisljeni_broj = random.randint(1, 100)
broj_pokusaja = 0

# GLAVNI DIO PROGRAMA
while True:
    uneseni_broj = int(input('Pogodite zamisljeni broj od 1 do 100: '))
    broj_pokusaja += 1
    
    if uneseni_broj == zamisljeni_broj:
        break
    elif uneseni_broj > zamisljeni_broj:
        print('Unijeli ste veci broj od zamisljenog broja.\n')

    elif uneseni_broj < zamisljeni_broj:
        print('Unijeli ste manji broj od zamisljenog broja.\n')
    


# PRIKAZ REZULTATA / KRAJ
print()
print(f'Cestitamo! Pogodili ste zamisljeni broj {zamisljeni_broj}')
print(f'Za to Vam je trebalo {broj_pokusaja} pokusaja.')
print()
