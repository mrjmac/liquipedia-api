import requests
from bs4 import BeautifulSoup
import argparse
parser = argparse.ArgumentParser(description='A working API for liquipedia VALORANT')
parser.add_argument('--player', type=str, help = 'the player that you want information on, enter their name with proper capitalization')

args = parser.parse_args()

URL = "https://liquipedia.net/valorant/" + args.player
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

results = soup.find(id = "mw-content-text")

info = results.find_all("div", style = "width:50%")
info2 = results.find_all("div", class_ = "infobox-cell-2")

dict = {}

i = 0
for fact in info :
    dict[info2[i].text.strip()] = fact.text.strip()
    i += 1    
    
print(dict)   


