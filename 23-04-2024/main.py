import requests
from bs4 import BeautifulSoup
import csv

def scrape_page(url):
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Failed to fetch data from: {url}. Status code is: {response.status_code}")
        return[]
    
    soup = BeautifulSoup(response.content, 'html.parser')
    table = soup.find('table')
    if table is None:
        print(f"No table found on the page which has url: {url}")
        return[]
    rows = table.find_all('tr')

    data = []
    for row in rows[1:]:
        cells = row.find_all('td')
        data.append([cell.text.strip() for cell in cells])
        # print(row)
    return data

def srcape_all_pages(base_url, num_pages):
    all_data = []
    for page_num in range(1, num_pages+1):
        url = f"{base_url}?page_num={page_num}"
        data = scrape_page(url)
        all_data.extend(data)
    return all_data

def main():
    base_url = "https://www.scrapethissite.com/pages/forms/"
    num_pages = 10
    all_data = srcape_all_pages(base_url, num_pages)
    

    with open('data.csv', 'w', newline='', encoding='utf-8') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(['Team Name', 'Year', 'Wins', 'Losses', 'OT Losses', 'Win %', 'Goals For (GF)', 'Goals Against (GA)', '+ / -'])
        csvwriter.writerows(all_data)

if __name__ == "__main__":
    main()



# Before executing code, Python interpreter reads source file and define few special variables/global variables. 
# If the python interpreter is running that module (the source file) as the main program, it sets the special
#  __name__ variable to have a value “__main__”. If this file is being imported 



