import requests
from bs4 import BeautifulSoup

baseurl = "https://starcofans.com"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'}

url = "https://starcofans.com/product/omega-inverter/"
# url = "https://starcofans.com/product/sapphire-inverter/"

# k = requests.get('https://starcofans.com/product/sapphire-inverter').text
# soup=BeautifulSoup(k,'html.parser')

r = requests.get(url)
htmlContent = r.content
soup = BeautifulSoup(htmlContent, 'html.parser')
prod = soup.find("button", class_="single_add_to_cart_button button alt")

if prod:
    print("Product Exists!")
    stock = soup.find("span", class_="woocommerce-Price-amount amount").get_text()
    print(stock)
    exit
else:
    print("Product Doesn't Exist!")
    exit

# stock = soup.find("button", class_="single_add_to_cart_button button alt").get_text()


# exit