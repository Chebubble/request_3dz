from pprint import pprint

import requests

url = 'https://akabab.github.io/superhero-api/api/all.json'
res = requests.get(url)

heroes = res.json()

our_heroes = filter(lambda hero: hero['name'] in ['Hulk', 'Captain America', 'Thanos'], heroes)
heroes_res = {hero['name']: hero['powerstats']['intelligence'] for hero in our_heroes}
print(max(heroes_res, key=heroes_res.get))

