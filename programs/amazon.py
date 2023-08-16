from bs4 import BeautifulSoup
import requests
from tkinter import messagebox
url = "https://www.bkmkitap.com/sefiller-2-cilt-takim-152098?gclid=CjwKCAjwq4imBhBQEiwA9Nx1BmGjnNMEQm7H6_oViOgVYwzghxPJ5IZsVmJeSufqADAHUYrljLTL9hoCQkIQAvD_BwE"

sayfa = requests.get(url)

html_sayfa = BeautifulSoup(sayfa.content,"html.parser")

isim = html_sayfa.find("h1",class_="fl col-12 text-regular m-top m-bottom").getText()
fiyat = html_sayfa.find("div",class_="col currencyPrice danger").getText()
yazar = html_sayfa.find("div",class_="yazarname fl col-12").getText()
yayım = html_sayfa.find("div",class_="fl col-12 text-center").getText()
yayımevi = yayım.split(" "); yayımevi = yayımevi[0]
print(fiyat,"TL")
print(yazar)
print(yayımevi)