''' Web Scraping

      Objective : To fetch the brand, description and price in csv file.
      Libraries : bs4 --> BeautifulSoup, urllib -->request-->urlopen
      Varibles  : uClient , page_html ,page_soup, containers, filename, f, headers, brand, title_container, product_name, shipping_container, price .'''



# Libraries #

import bs4
from urllib.request import  urlopen as uReq
from bs4 import BeautifulSoup as soup

# Given url #

my_url = "https://www.newegg.com/global/in/Product/ProductList.aspx?Submit=ENE&N=100203942%204802&IsNodeId=1&Description=graphics%20cards&name=Top%20Sellers&Order=BESTMATCH"

# Making connection a connection, download ans close the connection #

uClient = uReq(my_url)        # create the connection #
page_html = uClient.read()    # to download the file #
uClient.close()               # close the connection #

# Parsing a html file and by using soup function, we convert html text into data objects #

page_soup = soup(page_html,"html.parser")

# Here items starts with item- container class , so grab all functions by using finAll() #

containers = page_soup.findAll("div",{"class":"item-container"}) 

# Create the csv files and write the headings #

filename = "product.csv"
f =open(filename, "w")
headers = "Brand, Product Name, Price \n"
f.write(headers)

# Here we scrap the brand, item name and price an write in csv file. #
for container in containers:
    brand = container.div.div.a.img["title"]
    title_container = container.findAll("a", {"class": "item-title"})
    product_name = title_container[0].text
    shipping_container = container.findAll("li", {"class": "price-current"})
    price = shipping_container[0].text.encode('ascii','ignore').decode('UTF-8').strip().replace(',','')
    print("Brand : " + brand)
    print("Product Name :" + product_name)
    print("Price : " + price)
    f.write(brand + "," + product_name.replace(',', '|') + "," + price + "\n")
f.close()

#####   THE END   #####

