import requests as req
import bs4
import pandas as pd

def find_movie(url):
    html = req.get(url)
    soup = bs4.BeautifulSoup(html.text, "html.parser")
    blocks = soup.find_all("div", class_="release_movie_name")
    names = list()
    for block in blocks:
        name_ = block.find("a")
        names.append(name_)
    for name in names:
        print(name.text)
        print(name['href'])
    return names

file_name = list()
file_src = list()
for i in range(1, 5):
    url = "https://movies.yahoo.com.tw/onlinemovie_intheaters.html?page=%d" % i
    names = find_movie(url)
    for name in names:
        file_name.append(name.text.replace(" ", ""))
        file_src.append(name['href'])
    # print(url)

dataframe = pd.DataFrame({'name':file_name,'src':file_src})
dataframe.to_csv("test.csv")
