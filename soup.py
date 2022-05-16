from unicodedata import category
import requests
import urllib.request 
from bs4 import BeautifulSoup
from sqlalchemy import true
from urllib.error import HTTPError

names = []
dets = []

class Squish:
    def __init__(self, name, desc, img, sizes, categories):
        self.name = name
        self.desc = desc
        self.img = img
        self.sizes = sizes
        self.categories = categories
    def welcome(self):
        print(f"This is {' '.join(self.name)}: \n {self.desc} \n {self.img} \n {self.name[0]} comes in {self.sizes} \n and fits in with: {self.categories}")
        return 'done'



url = "https://squishmallowsquad.fandom.com/wiki/Master_List"
page = requests.get(url)
html = urllib.request.urlopen(url)

# parsing the html file
htmlParse = BeautifulSoup(html, 'html.parser')
substringt = '\t'
substringn = '\n'
# getting all the paragraphs
for para in htmlParse.find_all("a"):
    if (substringt not in para.get_text()):
        if (substringn not in para.get_text()):
            if('Master List' not in "title"):
                names.append(para.get_text())
urlList = []
def filtering(arr):
    for item in arr:
        if (len(item.split(" ")) == 3):
            urlList.append(item.split(" "))
filtering(names)


def run():
    i = 0
    while i < len(urlList)-1:
        name = urlList[i][0]
        baseurl = f"https://squishmallowsquad.fandom.com/wiki/{name}"
        i = i + 1
        try:
            html = urllib.request.urlopen(baseurl)
        except HTTPError as hp:
            print(hp, urlList[i-1])
        else:
            htmlParse = BeautifulSoup(html, 'html.parser')
            desc = htmlParse.find("blockquote")
            if (desc):
                desc = desc.get_text()
            else: 
                desc = "to come"
            img = htmlParse.find("img", attrs={"class": "pi-image-thumbnail"})
            if (img):
                img = img.get('src')
            else: 
                img = "to come"
            sizes = htmlParse.find_all("a")
            if (sizes):
                final_sizes = []
                categories = []
                for size in sizes:
                    title = size.get('title', 'No title attribute')
                    if 'Category' in title:
                        if 'inch' in title:
                            text = size.get_text()
                            if '"' not in text and text not in final_sizes:
                                final_sizes.append(text)
                        else:
                            text = size.get_text()
                            if text not in categories:
                                categories.append(text) 
            else:
                final_sizes.push('None')
                categories.push('None')
            dets.append(Squish(urlList[i-1], desc, img, final_sizes, categories))

run()

for det in dets:
    print([det.name,det.desc,det.img, det.sizes, det.categories], ",")