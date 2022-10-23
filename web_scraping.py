import requests
import requests_html
from bs4 import BeautifulSoup
from lxml import html
import urllib.request
holidayshome = []
requests.get('https://www.flightschoollist.com/airplane-flight-schools/')
with open("C:\pythondev\Airplanes.htm") as fp:
    soup = BeautifulSoup(fp, "html.parser")
    for cos in soup.find(id='usa').find_all("a", href=True, text=True):
      link_text  = cos["href"]
      print (link_text)
      teg=requests.get(link_text)
      soup = BeautifulSoup(teg.text, 'lxml')
      print("\nFind and print all td tags:\n")

      for tag in soup.find_all("td"):
           print("{0}: {1}".format(tag.name, tag.text))
















