import requests

def get(url):
    r = requests.get(url) # hämtar datan från den angivna urlen
    return r.json() # returnerar som en json objekt