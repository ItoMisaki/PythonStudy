import jieba
import requests
from bs4 import BeautifulSoup

url = "http://www.purepen.com/sgyy/002.htm"
res = requests.get(url)
res.encoding = "gb2312"

txt = ''

soup = BeautifulSoup(res.text, "html.parser")

for string in soup.stripped_strings:
    txt += string

for ch in ['\r', '\n', '\t', '&', '.', '_', '+']:
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
    print("{2:<2}:  {0:<20}{1:<10}".format(word, count, i+1))