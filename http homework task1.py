import requests

def get_strength_by_name(name):
    url =f'https://superheroapi.com/api/2619421814940190/search/{name}'
    response = requests.get(url)
    res = response.json()
    strength = res['results'][0]['powerstats']['strength']
    return int(strength)

list= ['Hulk','Captain America','Thanos']
maxt ={}
for i in list:
    maxt[i] = get_strength_by_name(i)
    max_value = max(maxt.values())
    final_dict = {k: v for k, v in maxt.items() if v == max_value}
print(final_dict)
