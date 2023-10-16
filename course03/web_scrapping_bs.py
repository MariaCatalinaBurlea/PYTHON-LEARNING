from bs4 import BeautifulSoup
import requests

request_page = requests.get("https://www.bnr.ro/Cursul-de-schimb--7372.aspx")
link = BeautifulSoup(request_page.text, "html.parser")

main = link.find_all('div', attrs={'id': 'contentDiv'})
for obj in main:
    for table_index in obj.find_all("table"):
        for table_tr in table_index.f