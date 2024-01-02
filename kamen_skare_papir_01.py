'''
Igra:   Kamen Skare Papir
Autor:  Karlo Karadjole
Datum:  02.01.2024.
'''


import random

pobjeda_korisnika = 0
pobjeda_kompjutera = 0

opcije = ['kamen' , 'papir', 'skare']

while True:
    unos_korisnika = input('Unesite kamen/papir/skare ili Izlaz za prekid igre: ').lower()
    if unos_korisnika == 'izlaz':
        break

    if unos_korisnika not in opcije:
        continue
    
    random_broj = random.randomint(0, 2)
    # kamen 0, papir 1, skare 2
    izbor_kompjutera = opcije[random_broj]
    print('Computer je izabrao', izbor_kompjutera + '.')

    if unos_korisnika == 'kamen' and izbor_kompjutera == 'skare':
        print('Naša pobjeda')
        pobjeda_korisnika += 1

    elif unos_korisnika == 'papir' and izbor_kompjutera == 'kamen':
        print('Naša pobjeda')
        pobjeda_korisnika += 1
    
    elif unos_korisnika == 'skare' and izbor_kompjutera == 'papir':
        print('Naša pobjeda')
        pobjeda_korisnika += 1

    else:
        pobjeda_kompjutera += 1

print('Mi smo pobjedili', pobjeda_korisnika, 'puta.')
print('Kompjuter je pobjedio', pobjeda_kompjutera, 'puta.')
print()