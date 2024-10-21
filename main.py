
import requests

print("hello World !")
r = requests.get('https://epsi.fr')
print(r.text)