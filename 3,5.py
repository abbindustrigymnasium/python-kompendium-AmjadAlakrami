#skapar listor
male = [
"Erik",
"Lars",
"Karl",
"Anders",
"Johan"
]
female = [
"Maria",
"Anna",
"Margareta",
"Elisabeth",
"Eva"
]

# input variablar
a = input("vilket namn vill du ta bort från listan "+ str(male)) 
b = input("vilket namn vill du ta bort från listan"+ str(female))

male.remove (a) # ta bort den användaren matade in i input a från male listaan 
female.remove(b)

# printa ut 
print(male)
print(female)


