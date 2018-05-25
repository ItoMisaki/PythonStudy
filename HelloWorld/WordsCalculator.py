import jieba
import requests
from bs4 import BeautifulSoup

txt = ''

urlbase = "http://weixin.sogou.com"
resbase = requests.get(urlbase)
resbase.encoding = "utf-8"

soupbase = BeautifulSoup(resbase.text, "html.parser")

for link in soupbase.find_all('a'):
    if str(link.get('href')).startswith("http"):
        print(str(link.get('href')))
        res = requests.get(link.get('href'))
        res.encoding = "utf-8"
        soup = BeautifulSoup(res.text, "html.parser")
        txt += soup.get_text()

for ch in ['\r', '\n', '\t', '&', '.', '_', '+', '#', '%']:
    txt = txt.replace(ch, ' ')


words = jieba.lcut(txt)
counts = {}

for word in words:
    if len(word) == 1:
        continue
    elif word[0].lower() in "abcdefghijklmnopqrstuvwxyz0123456789":
        continue
    else:
        counts[word] = counts.get(word, 0) + 1

items = list(counts.items())
items.sort(key=lambda x: x[1], reverse=True)

for i in range(min(len(items), 20)):
    word, count = items[i]
    print("{2:<2}:  {0:{3}<10}{1:<5}".format(word, count, i+1, chr(12288)))
