
import requests
from bs4 import BeautifulSoup
import csv

root_url = "https://www.lookup.pk/dynamic/search.aspx?searchtype=kl&k=gym&l=lahore"
html = requests.get(root_url)
soup = BeautifulSoup(html.text, 'html.parser')

paging = soup.find("div",{"class":"pg-full-width me-pagination"}).find("ul",{"class":"pagination"}).find_all("a")
start_page = paging[1].text
last_page = paging[len(paging)-2].text


outfile = open('gymlookup.csv','w', newline='')
writer = csv.writer(outfile)
writer.writerow(["Name", "Address", "Phone"])


pages = list(range(1,int(last_page)+1))
for page in pages:
    url = 'https://www.lookup.pk/dynamic/search.aspx?searchtype=kl&k=gym&l=lahore&page=%s' %(page)
    html = requests.get(url)
    soup = BeautifulSoup(html.text, 'html.parser')

    #print(soup.prettify())
    print ('Processing page: %s' %(page))

    product_name_list = soup.findAll("div",{"class":"CompanyInfo"})
    for element in product_name_list:
        name = element.find('h2').text
        address = element.find('address').text.strip()
        phone = element.find("ul",{"class":"submenu"}).text.strip()

        writer.writerow([name, address, phone])

outfile.close()
print ('Done')

