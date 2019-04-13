import math # importerar math bibloteket


a = input("Hur många elever vill ha 2 Vanilga korvar ?") # input variabel 
b = input("Hur många elver vill ha 3 Vanliga korvar ? ")
c = input("Hur många elever vill ha 2 Veganska korvar ?")
d = input("Hur många elever vill ha 3 veganska korvar ?")
g = input ("Hur många elever vill ha en dryck? ")

e = (2 * int(a)) + (3 * int(a)) #variabel e = 2 * a + 3 * a, där a är en int 
f = (2 * int(c)) + (3 * int(d))

print ("Vanlig Korv:" + " " + str(math.ceil((int(e)/8) )) + " " + "Förpackningar" )  # printar ut vanliga korv + variabel e/8 .. vi använder math.ceil funktionen från math biblotek för att avrunda uppåt 
print ("Veganska Korv:" + " " + str(math.ceil((int(f)/4) ))+ " " + "Förpackningar")
print ("Dryckor:" + " " + str(g))

h = int(str(math.ceil((int(e)/8) ))) * float (20.95)
i = int(str(math.ceil((int(f)/4) )))* float (34.95)
j = int(g) * float(13.95)
k= int(h) + int(i) + int(j)
print ("Det kostar totalt:" + " " + str(k) + " " + "SEK")

