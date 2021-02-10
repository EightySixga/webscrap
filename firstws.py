#import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
my_url= 'https://www.newegg.com/p/pl?d=Graphics+card'
uClient= uReq(my_url)
page_html = uClient.read()
uClient.close()
# html parse
page_soup= soup(page_html,"html.parser")
page_soup.h1
#find item graphics card
containers = page_soup.findAll("div",{"class":"item-container"})
filename="products.csv"
f=open(filename,"w")
headers="grapics card features\n"
f.write(headers)
len(containers)
contain=containers[0]
container=containers[0]
for container in containers:
	#brand=container.div.div.a.img[0].text
	title_container=container.findAll("a",{"class":"item-title"})
	product_name=title_container[0].text
	shipping_container=container.findAll("li",{"class":"price-ship"})
	shipping=shipping_container[0].text

#print("brand:" +brand)
	print("product_name:"+product_name)
	print("shipping:"+shipping)
	f.write(product_name.replace(",","|")+","+shipping+"\n")
f.close()
