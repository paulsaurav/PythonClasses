import requests
from bs4 import BeautifulSoup
import csv

url = 'https://www.scrapethissite.com/pages/simple/'

response = requests.get(url)
response.raise_for_status() #This will raise an exception for HTTP errors

soup = BeautifulSoup(response.content, "html.parser")

countries = soup.find_all('div', class_='country')

country_data = []

for country in countries:
    name = country.find('h3', class_='country-name').text.strip()

    name = name.replace(country.find('i').text, '').strip()

    capital = country.find('span', class_='country-capital').text.strip()

    population = country.find('span', class_='country-population').text.strip()

    area = country.find('span', class_='country-area').text.strip()

    country_data.append({
        'Country': name,
        'Capital': capital,
        'Population': population,
        'Area': area
    })

for data in country_data:
    print(data)

csv_file = 'Country_data.csv'

with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=['Country','Capital','Population','Area'])
    writer.writeheader()
    writer.writerows(country_data)
print(f"Data has been stored to{csv_file}")