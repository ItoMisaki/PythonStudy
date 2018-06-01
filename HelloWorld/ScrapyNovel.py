from bs4 import BeautifulSoup
import os
import time
import requests
import random
'''
根据url、http headers获取http报文
参数：req_url 
     req_headers
     req_proxy
返回：target_html 或者 None
'''


def get_html_text(req_url, req_headers, req_proxy):
    target_html = None
    try:
        time.sleep(0.5 + random.random())
        target_response = requests.get(req_url, timeout=30, params=req_headers, proxies=req_proxy)
        target_response.raise_for_status()
        target_response.encoding = target_response.apparent_encoding
        target_html = target_response.content
    except:
        print("访问失败{0:<3}: {1}".format(target_response.status_code, target_response.url))
    finally:
        return target_html



'''
根据html报文内容，检索出小说内容的URL字典
参数：html_text, base_url="http://www.biqukan.com"
返回：dict_urls, url_numbers, novel_name
'''


def find_contents_url(html_text, base_url="http://www.biqukan.com"):
    url_numbers = 0
    url_dict = dict()

    bs_parent = BeautifulSoup(html_text, "html.parser")
    listmain = bs_parent.find_all("div", class_='listmain')
    bs_url = BeautifulSoup(str(listmain), "html.parser")

    if bs_url.dt and bs_url.dt.string:
        novel_name = str(bs_url.dt.string).split("》")[0].split("《")[1]
        flag_name = "《" + novel_name + "》" + "正文卷"
        flag_begin = False

        for bs_child in bs_url.dl.children:
            if bs_child != '\n':
                if bs_child.string == flag_name:
                    flag_begin = True
                if (flag_begin == True) and (bs_child.a != None):
                    download_url = base_url + bs_child.a.get('href')
                    download_name = bs_child.string
                    url_dict[download_name] = download_url
                    url_numbers += 1
    else:
        novel_name = ""

    return url_dict, url_numbers, novel_name


'''
根据报文内容，获取章节内容
参数：html_text
返回：chapter_text
'''


def get_chapter_contents(html_text):
    chapter_text = None
    try:
        soup_texts = BeautifulSoup(html_text, 'html.parser')
        texts = soup_texts.find_all(id='content', class_='showtxt')
        chapter_text = BeautifulSoup(str(texts), 'html.parser').div.text.replace('\xa0', '')
    except:
        print("解析htlm失败：" + str(html_text))
    finally:
        return chapter_text

'''
将获取的章节内容写入文件
参数：path, title, text
返回：
'''


def write_to_file(path, title, text, code='utf-8'):
    write_flag = True
    with open(path, 'a', encoding=code) as f:
        f.write(title + '\n\n')
        for each in text:
            if each == 'h':
                write_flag = False
            if write_flag == True and each != ' ':
                f.write(each)
            if write_flag == True and each == '\r':
                f.write('\n')
        f.write('\n\n')


if __name__ == '__main__':

    target_url = "http://www.biqukan.com/1_1719/"
    target_headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.2; WOW64; rv:21.0) Gecko/20100101 Firefox/21.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
    }
    target_proxy = {'https': '123.139.56.238:999'}

    print("小说地址: " + target_url)

    html = get_html_text(target_url, target_headers, target_proxy)
    if html is None:
        print("获取章节目录失败: {0}".format(target_url))

    else:
        download_url, chapter_nums, novel_name = find_contents_url(html)

        print("小说名称：" + novel_name + " 章节数量：" + str(chapter_nums))
        print("开始下载".center(20, "*"))

        if novel_name + ".txt" in os.listdir():
            os.remove(novel_name + ".txt")

        index = 1

        for key, value in download_url.items():
            chapter_html = get_html_text(value, target_headers, target_proxy)
            if chapter_html:
                chapter_text = get_chapter_contents(chapter_html)
                chapter_name = str(key)
                write_to_file(novel_name + ".txt", chapter_name, chapter_text)
                print("已下载:{0:.3f}%: {1}: {2}".format(float(index * 100 / chapter_nums), chapter_name, str(value)))
                index += 1
            else:
                print("获取章节内容失败: {0}:{1}".format(key, value))

        print("结束下载".center(20, "*"))