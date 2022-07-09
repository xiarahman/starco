from concurrent.futures import process
import requests
from bs4 import BeautifulSoup
import time
from send_mail import send_email

baseurl = "https://starcofans.com"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'}

# product_url = "https://starcofans.com/product/omega-inverter/"
product_url = "https://starcofans.com/product/sapphire-inverter/"

# k = requests.get('https://starcofans.com/product/sapphire-inverter').text
# soup=BeautifulSoup(k,'html.parser')


# Scrap product
def find_product(url=product_url):
    r = requests.get(url)
    htmlContent = r.content
    soup = BeautifulSoup(htmlContent, 'html.parser')
    prod = soup.find(
        "button", class_="single_add_to_cart_button button alt")

    if prod:
        print("Product Exists!")
        product = soup.find("div", class_="et_pb_module_inner").get_text()
        product = "Exist: "+product
        print(product)
        stock = soup.find(
            "span", class_="woocommerce-Price-amount amount").get_text()
        print(stock)
        send_email(product, stock)
        # exit
    else:
        print("Product Doesn't Exist or Out of stock!")
        # exit


# Call scrapper
find_product()

# Timed scrap with intervals


def timed_scrapper():
    while(True):
        r = requests.get(url)
        htmlContent = r.content
        soup = BeautifulSoup(htmlContent, 'html.parser')
        prod = soup.find(
            "button", class_="single_add_to_cart_button button alt")

        if prod:
            print("Product Exists!")
            stock = soup.find(
                "span", class_="woocommerce-Price-amount amount").get_text()
            print(stock)
            send_email('Product Exists', stock)
            # exit
        else:
            print("Product Doesn't Exist!")
            # exit
        time.sleep(30)

# stock = soup.find("button", class_="single_add_to_cart_button button alt").get_text()


exit
