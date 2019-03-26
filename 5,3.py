norden = ["Danmark", "Finland", "Island", "Norge", "Sverige"]
storbritanien = ["England", "Norderland", "Skottland", "Wals"]
a = input("vilket land kommer du ifrån?")
if a.title() in norden: 
     print ("landet är en del av norden")
elif a.title in storbritanien :
    print ("landet är en del av storbritanien ")
else :
    print("landet tillhör inte storbritanien eller norden")