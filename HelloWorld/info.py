import requests
from bs4 import BeautifulSoup
import bs4
import time

def getHtmlText(url):
    rs = requests.Response()
    try:
        rs = requests.get(url, timeout=60, params={"User-Agent": "Mozilla/5.0"})
        rs.raise_for_status()
        rs.encoding = rs.apparent_encoding
        return rs.text
    except:
        print("访问失败{0:<3}:{1}".format(rs.status_code, rs.url))
        return ""

def fillNetValList(netVallist, html):
    soup = BeautifulSoup(html, "html.parser")
    for tr in soup.find("tbody").children:
        if isinstance(tr, bs4.element.Tag):
            tds = tr('td')
            netVallist.append([tds[0].text.strip("\n"),
                              tds[1].string.strip("\n"),
                              tds[2].string.strip("\n \r\t"),
                              tds[3].string.strip("\n"),
                              tds[4].string.strip("\n"),
                              tds[6].string.strip("\n")])


def outputNetValList(netVallist, filepath):
    try:
        f = open(filepath, "wt", encoding="utf_8_sig")
        f.write("基金名称,基金代码,类型,净值日期,单位净值,日涨跌(%)\n")
        for i in range(len(netVallist)):
            netVal = netVallist[i]
            f.write(netVal[0] + ","
                         + netVal[1] + ","
                         + netVal[2] + ","
                         + netVal[3] + ","
                         + netVal[4] + ","
                         + netVal[5] + "\n")
        f.close()
    except:
        print("打开/写入文件{}失败！".format(filepath))
    finally:
        print("程序运行结束")
        if f:
            f.close()

def main():
    netValueList = []
    url = "http://www.xqfunds.com"

    rs = getHtmlText(url)

    fillNetValList(netValueList, rs)

    outputNetValList(netValueList, time.strftime('%Y-%m-%d', time.localtime(time.time()))+".csv")

main()

