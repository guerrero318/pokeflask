import requests

URL="http://127.0.0.1:2224/json"

response=requests.get(URL).json()


for poke in response:
    print(f"""{poke['name']} has an ID of {poke['id']} and is a {'/'.join(poke['type'])} type.""")