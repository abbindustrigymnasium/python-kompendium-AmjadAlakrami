Kim_kardishian = ["svart", "kvinna", "grön"]
Hillary_Clinton = ["blond", "kvinna", "blå"]
Zayn_Malik = ["svart", "man", "brun"]
Trump = ["röd", "man", "blå"]
Kön = input("Ange ditt kön" +  "(man/kvinna)")
Hårfärge = input("Vad har du för hår färg?")
Ögonfärg = input("Vad har du för färg på dina ögon?")

if Kön in Zayn_Malik:
    if Hårfärge in Zayn_Malik:  
        if Ögonfärg in Zayn_Malik:
            print("Du liknar Zayn Malik")
elif Kön in Trump:
    if Hårfärge in Trump:  
        if Ögonfärg in Trump:
            print("Du liknar Trump")

elif Kön in Kim_kardishian:
    if Hårfärge in Kim_kardishian:  
        if Ögonfärg in Kim_kardishian:
            print("Du liknar Kim Kardishian")
elif Kön in Hillary_Clinton:
    if Hårfärge in Hillary_Clinton:  
        if Ögonfärg in Hillary_Clinton:
            print("Du liknar Hillary Clinton")
else :
    print("Du är unik")
