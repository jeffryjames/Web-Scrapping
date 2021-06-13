# use pip install autoscraper to install
#import
from autoscraper import AutoScraper

#url from where the pattern is to be extracted
url = "https://www.jiomart.com/c/groceries/dairy-bakery/dairy/62"
#Details of the Module to be extracted
wanted_list=["Amul Elaichi Shrikhand 500 g (Container)","₹ 93.00","https://www.jiomart.com/images/product/150x150/590067375/amul-elaichi-shrikhand-500-g-container-0-20210324.jpg"]

scraper = AutoScraper()
scraper.build(url,wanted_list)

# link of other pages from where datas are collected
data = scraper.get_result_similar("https://www.jiomart.com/c/groceries/snacks-branded-foods/extracts-flavouring/181",grouped=True)
data
# to list keys and select only needed keys from it
keys = list(data.keys())
print(keys)

a = data[str(keys[0])]
a

b = data[str(keys[3])]
b

c = data[str(keys[-1])]
c

#to save the output to file for first time
import csv

filename = "products.csv"
f = open(filename, "a")
with open(filename,"a",encoding="utf-8") as file:
    writer = csv.writer(file)
    for i in range(0,len(a)):
        writer.writerow([str(a[i]),str(b[i]),str(c[i])])
        

# ..........to append the data of output to file after it is created........

#import csv

#filename = "products.csv"
#f = open(filename, "w")
#with open(filename,"w",encoding="utf-8") as file:
  #  writer = csv.writer(file)
  #  for i in range(0,len(a)):
    #    writer.writerow([str(a[i]),str(b[i])])

