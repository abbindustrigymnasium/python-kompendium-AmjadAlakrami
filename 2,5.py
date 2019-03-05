import math

def roundup(a, digits=0):
    n = 10**-digits
    return round(math.ceil(a / n) * n, digits)

a = input("Hur många elever vill ha 2 Vanilga korvar ?")
b = input("Hur många elver vill ha 3 Vanliga korvar ? ")
c = input("Hur många elever vill ha 2 Veganska korvar ?")
d = input("Hur många elever vill ha 3 veganska korvar ?")
g = input ("Hur många elever vill ha en dryck? ")

e = (2 * int(a)) + (3 * int(a))
f = (2 * int(c)) + (3 * int(d))

print ("Vanlig Korv:" + " " + str(roundup((int(e)/8), 0 )) + " " + "Förpackningar" )
print ("Veganska Korv:" + " " + str(roundup((int(f)/4), 0 ))+ " " + "Förpackningar")
print ("Dryckor:" + " " + str(g))

h = int(str(roundup((int(e)/8), 0 ))) * float (20.95)
i = int(str(roundup((int(f)/4), 0 )))* float (34.95)
j = int(g) * float(13.95)
k= int(h) + int(i) + int(j)
print ("Det kostar totalt:" + " " + str(k) + " " + "SEK")





