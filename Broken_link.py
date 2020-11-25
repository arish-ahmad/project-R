from bs4 import BeautifulSoup
from urllib.request import urlopen
import re,requests,os
from csv import DictWriter,writer

url = "https://cbdbene.com/"
def all_links(url):
    web_links=[]
    req = requests.get(url)
    soup = BeautifulSoup(req.text, "html.parser")
    for link in soup.find_all('a'):
        web_links.append(link.get('href'))
    new_list=[]
    for link in web_links:
        if link != None:
            new_list.append(link)     # Filter  list with removing none and "/" url
    res_list=[]         
    for i in  new_list:
        temp=str(i).split('/')[-1]
        if temp != "":
            res_list.append(temp)            #final list of all webpages
    images = []       
    for i in res_list:
        try:
            html_page = urlopen(url+i)
            soup = BeautifulSoup(html_page,"html.parser")
            for img in soup.findAll('img'):   
                images.append(img.get('src'))    #summarized list of all images urls of Each webpage
        except:
            pass
    return images
images_link=all_links(url)  #this list contain the urls of all images used in website
broken_links=[]
for link in images_link:
    if 'https' not in  link:
        if requests.head(url+link).status_code != 200:
            broken_links.append(url+link)
    else:
        if requests.head(link).status_code != 200:
            broken_links.append(link)           #this list contain of all broken links

filename="Broken_links.csv"            # creating ms-excel file
file_exists=os.path.isfile(filename)
with open(filename,"a",newline="") as f:
    csv_writer=DictWriter(f,fieldnames=['Broken_links'])
    if not file_exists:
        csv_writer.writeheader()
        for links in broken_links:
            csv_writer.writerow({
                'Broken_links':links
            })