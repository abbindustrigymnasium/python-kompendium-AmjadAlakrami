m = range(1000000) # vi använder en inbygd funktion (range) som liknar listor för att sätta variabelen m storlek 

a = 0 # variabel a = 0 

for nummer in m : # for loop .. definerar variabel nymmer som alla variabel i m .. för varje nummer i m 

    summa = a + nummer # addera nummer med a 

#det for loopen gör är att det går i "listan" m o addera första värdet i listan med a, sedan går in i listan igen och adderar andra värdet med summan av den föra additionen osv 

print(summa)  # printa ut summa

