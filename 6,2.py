import requests
a = input ("ange en stad " + ":"+ "")
r = requests.get('https://54qhf521ze.execute-api.eu-north-1.amazonaws.com/weather/' + a)
res = r.json()
for d in res ['forecasts']:
    print (d["date"])
    print (d["date"])
    

