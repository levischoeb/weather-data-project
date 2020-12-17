# imports first
import requests
import pandas as pd
from bs4 import BeautifulSoup


# load html page and parse
page = requests.get("https://ch.wetter.com/wetter_aktuell/wettervorhersage/7_tagesvorhersage/schweiz/sankt-gallen/CH0CH3756.html")
soup = BeautifulSoup(page.content, 'html.parser')

# dict will hold data
listings = []

# get rid of surrounding garbage
grid = soup.find(class_="spaces-weather-grid")

# "today" is a separate class
for day in soup.find_all(class_= ["swg-row-wrapper bg--blue-gradient text--white",
                                  "swg-row-wrapper bg--blue-gradient text--white is-selected"]):


    # get all the rows
    texts = day.find_all(class_="swg-row")

    # cherry-pick relevant pieces (could be more elegant)
    date = texts[0].get_text().replace("  ", "") #remove spaces
    date = date.replace("\n", "") #remove newlines

    descriptor = texts[1].get_text().replace("  ", "")
    descriptor = descriptor.replace("\n", "")

    temp = texts[3].get_text().replace("\n", "")
    temp = temp.split("/\u2009") #remove symbols

    tempMax = temp[0]
    tempMin = temp[1]

    chanceOfPrec = texts[6].get_text().replace("  ", "")
    chanceOfPrec = chanceOfPrec.replace("\n", "")
    chanceOfPrec = chanceOfPrec.replace("\u202f", " ")

    precipitation = texts[8].get_text().replace("\n", "").replace("\u202f", " ").replace("  ", "")

    windDir = texts[9].get_text().replace("\n", "").replace("\xa0", "").replace("  ", "")

    windSpeed = texts[10].get_text().replace("\n", "").replace("\u202f", " ").replace("  ", "")

    new_dict = {"date" : date, "desc" : descriptor, "tempMax": tempMax,
                "tempMin": tempMin, "chanceOfPrec": chanceOfPrec,
                "windDir": windDir, "windSpeed": windSpeed}

    listings.append(new_dict)


df = pd.DataFrame(listings)

print(df)
