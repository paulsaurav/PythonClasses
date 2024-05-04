import requests
from bs4 import BeautifulSoup

url = 'https://www.scrapethissite.com/pages/simple/'

response = requests.get(url)
# print(response)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, "html.parser")
    # print(soup)

    kiran = soup.find_all("h3")

    for bishal in kiran:
        print(bishal)

    
else:
    print("Failure")

