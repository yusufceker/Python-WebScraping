from bs4 import BeautifulSoup
import requests
from tkinter import messagebox
url = "https://www.trendyol.com/apple/iphone-11-64-gb-siyah-cep-telefonu-aksesuarsiz-kutu-apple-turkiye-garantili-p-64074791?boutiqueId=61&merchantId=147122"

response = requests.get(url)

soup = BeautifulSoup(response.content,"html.parser")

iPhone11_price = soup.find("span",class_="prc-dsc").getText()

iPhone11_model = soup.find("span",text=" iPhone 11 64 GB Siyah Cep Telefonu Aksesuarsız Kutu (Apple Türkiye Garantili) ").getText()

iPhone11_memory = soup.find("span",class_="attribute-value",text="64 GB").getText()


messagebox.showinfo("iPhone 11","Model: {}\nFiyat: {}\nHafıza: {}".format(iPhone11_model,iPhone11_price,iPhone11_memory))

