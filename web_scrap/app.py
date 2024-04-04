from flask import Flask

app = Flask(__name__)



import pandas as pd
import requests
from bs4 import BeautifulSoup
Product_name=[]
Prices=[]
Description=[]
Reviews=[]

for i in range(2,12):
    url="https://www.flipkart.com/search?q=mobiles+under+50000&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page="+str(i)
    r=requests.get(url)
    #print(r)
    soup=BeautifulSoup(r.text,"lxml")
    

    names = soup.find_all("div",class_="_4rR01T")
    for i in names:
        name = i.text
        Product_name.append(name)
    #print(Product_name)

    prices=soup.find_all("div",class_="_30jeq3 _1_WHN1")

    for i in prices:
        name=i.text
        Prices.append(name)
    #print(Prices)

    desc=soup.find_all("ul",class_="_1xgFaf")

    for i in desc:
        name=i.text
        Description.append(name)
    #print(Description)

    


#print(len(Reviews))


    #print(soup)
    #while True:
    #np=soup.find("a",class_="_1LKTO3").get("href")
    #cnp="https://www.flipkart.com"+np
    #print(cnp)


    #url=cnp
    #r=requests.get(url)
    #soup=BeautifulSoup(r.text,"lxml")
    
    
df=pd.DataFrame({"Product Names":Product_name,"Price":Prices,"Description":Description})
df.to_csv("C:/Users/aipee/OneDrive/Pictures/Flipkart_mobiles_under_50000.csv")


if __name__=="__main__":
    app.run(host="0.0.0.0")
