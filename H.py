
# HTML Scraping
from bs4 import BeautifulSoup
import requests
import csv

data = []

def scrape_data(search_year):
    year_data = []
    url = 'https://en.wikipedia.org/wiki/Billboard_Year-End_Hot_100_singles_of_' + str(search_year)
    r = requests.get(url).text

    soup = BeautifulSoup(r, 'html.parser')
    table = soup.find('table', attrs={'class': 'wikitable'})
    rows = table.find_all('tr')

    for row in rows[1:]:
        cols = row.find_all(['td', 'th'])
        year_data.append([col.text for col in cols])

    for n in year_data:
        n.insert(0, search_year)

    return year_data

for year in range(2000, 2020):
    try:
        data.append(scrape_data(year))
        print('Scraping data for:', year)
    except AttributeError as e:
        print(year, "doesn't have the data your looking for, stopping...")
        break

writer = csv.writer(open('songs.csv', 'w'), delimiter=',', lineterminator='\n', quotechar='"')
for years in data:
    for songs in years:
        writer.writerow(songs)





