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

info = results.find_all("div", class_ = "infobox-cell-2")

dict = {}

i = 1
for fact in info :
    if fact.text.strip() == "" :
        test = fact.find_all("a")
        information = ""
        for thing in test :
            img = thing.find('img', alt=True)
            information += img['alt'] + "\n"

    if i % 2 == 0 :
        if fact.text.strip() != "" :
            information = fact.text.strip()
        dict[name.replace(" ", "")] = information
    else :
        name = fact.text.strip()
    i += 1
    
    
print(dict)   


