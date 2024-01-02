# kamen, skare, papir
# kamen > skare
# kamen < papir
# skare > papir
# skare < kamen
# papir > kamen
# papir < skare

# IMPORT
import random

# DEKLARACIJA
izbornik = '''
    Izbornik opcija (upisite broj ispred opcije):
    1. kamen
    2. skare
    3. papir
'''
broj_partija = 0
bodovi_korisnik = 0
bodovi_racunalo = 0

# GLAVNI PROGRAM - MAIN
while broj_partija < 3:
    izbor_racunala = random.randint(1, 3)
    print(izbor_racunala)
    print()
    print(izbornik)
    print()

    while True:
        izbor_korisnika = int(input('Izaberite jednu od ponudenih opcija: '))

        if izbor_korisnika in [1, 2, 3]:
            break
        else:
            print('Krivo ste unijeli')


    # PROVJERA POBJEDNIKA PARTIJE
    if izbor_korisnika == izbor_racunala:
        print('Nerijeseno')
        broj_partija += 1
    
    #   kamen                           skare
    elif izbor_korisnika == 1 and izbor_racunala == 2:
        print('Korisnk je osvojio jedan bod')
        bodovi_korisnik += 1
        broj_partija += 1
    
    #   kamen                           papir
    elif izbor_korisnika == 1 and izbor_racunala == 3:
        print('Racunalo je osvojilo jedan bod')
        bodovi_racunalo += 1
        broj_partija += 1

    #   skare                           kamen
    elif izbor_korisnika == 2 and izbor_racunala == 1:
        print('Racunalo je osvojilo jedan bod')
        bodovi_racunalo += 1
        broj_partija += 1

    #   skare                           papir
    elif izbor_korisnika == 2 and izbor_racunala == 3:
        print('Korisnk je osvojio jedan bod')
        bodovi_korisnik += 1
        broj_partija += 1

    #   papir                           kamen
    elif izbor_korisnika == 3 and izbor_racunala == 1:
        print('Korisnk je osvojio jedan bod')
        bodovi_korisnik += 1
        broj_partija += 1

    #   papir                           skare
    elif izbor_korisnika == 3 and izbor_racunala == 2:
        print('Racunalo je osvojilo jedan bod')
        bodovi_racunalo += 1
        broj_partija += 1


# KRAJ
if bodovi_racunalo > bodovi_korisnik:
    print("Izgubili ste")
elif bodovi_racunalo < bodovi_korisnik:
    print("Pobijedili ste")
else:
    print("Nerijeseno")
