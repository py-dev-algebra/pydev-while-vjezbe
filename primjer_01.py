
# Deklaracija
my_list = [8, 6, 12, 14, 122]
to_find = 14
is_found = False


# Glavni dio programa
for i in range(len(my_list)): # range(5) -> raspon cijelih brojeva od 0 do 4
    # if my_list[i] == to_find:
    #     is_found = True
    is_found = my_list[i] == to_find # -> kraci zapis prethodne dvije linije
    if is_found:
        break

# Zavrsetak / Prikaz podataka
if is_found == True:  #or just  ->  if found:
    print("Element found at index", i)
else:
    print("Absent")