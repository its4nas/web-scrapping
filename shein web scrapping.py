#first step ----> import all libraries that are requierd
import requests
from bs4 import BeautifulSoup
import csv
from itertools import zip_longest



# products_prices_US = []
# products_prices_SR = []

#second step -----> use requests to fetch the url
result = requests.get("https://ar.shein.com/Men-Activewear-c-2443.html?adp=10850569&src_module=Men&src_identifier=on%3DIMAGE_COMPONENT%60cn%3Dshopbycate%60hz%3DhotZone_8%60ps%3D3_8%60jc%3Dreal_2443&src_tab_page_id=page_home1691871919028&ici=CCCSN%3DMen_ON%3DIMAGE_COMPONENT_OI%3D5920103_CN%3DONE_IMAGE_COMPONENT_TI%3D50001_aod%3D0_PS%3D3-8_ABT%3D0")


#third step -----> save page content
src = result.content
# print(src)

#fourth step -----> create soup object to parse content
soup = BeautifulSoup(src, "lxml")
# print(soup.find('a'))
# print(soup)

#fifth step -----> find the elements contaning info we need
# like Product_name, Price, Photos, Colors ...etc
products_name = soup.find_all("a" , {"class" : "S-product-item__link_jump S-product-item__link"})
# products_price = soup.find_all("p", {"class" : "product-item__camecase-wrap"})
# print(products_name)

products_names = []
# sixth step -----> loop over returned lists to extract needed info into other lists
for i in range(len(products_names)):
    products_names.append(products_name[i].text)

print(products_names)
