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

a = input("vilket namn vill du ta bort från listan "+ str(male))
b = input("vilket namn vill du ta bort från listan"+ str(female))

male.remove (a)
female.remove(b)
print(male)
print(female)

