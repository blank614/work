#!/usr/bin/env python
# -*- coding:utf-8 -*-

import requests
import time
import os
import pdfkit
from bs4 import BeautifulSoup
urls = []
for i in range(5,9):
    url = "http://cloudman.blog.51cto.com/all/10425448/page/"
    url = url + str(i)

    # header = {'User-Agent':
    #              'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'}
    req = requests.get(url)
    soup = BeautifulSoup(req.content, "html5lib")
    link=soup.find_all(class_="modCon")[2]
    # 遍历多少页
    for li in link.find_all("li"):
        url = "http://cloudman.blog.51cto.com" + li.a.get('href')
        urls.append(url)
    # print urls


for i in range(urls.__len__()):
    response = requests.get(urls[i])
    soup = BeautifulSoup(response.content, "html5lib")

    body = soup.find_all(class_="showBox")[0]
    html = str(body)
    title = soup.find_all("title")
    title = soup.title.string
    title=str(soup.title.string).split(" - CloudMan")[0]
    number=title.split("（")[1]
    title=title.split("（")[0]
    number=number.split("）")[0]+'、'
    title='E:\\pdf\\'+number+title+'.pdf'
    print(title)
    # title=u"%s.pdf" % title
    # print type(title)
    with open("a.html", 'w',encoding='utf-8') as f:
        f.write("""
<html>
<head>
<meta http-equiv="content-type" content="text/html;charset=utf-8">
<body>
""")
        f.write(html)
        f.write("""
</body>
</head>
</html>""")
    time.sleep(5)
    options = {
        'page-size': 'Letter',
        'margin-top': '0.75in',
        'margin-right': '0.75in',
        'margin-bottom': '0.75in',
        'margin-left': '0.75in',
        'encoding': "UTF-8",
        'custom-header': [
            ('Accept-Encoding', 'gzip')
        ],
        'cookie': [
            ('cookie-name1', 'cookie-value1'),
            ('cookie-name2', 'cookie-value2'),
        ],
        'outline-depth': 10,
    }
    config = pdfkit.configuration(wkhtmltopdf=r"C:\Python27\wkhtmltopdf\bin\wkhtmltopdf.exe")
    pdfkit.from_file('a.html', title, options=options, configuration=config)
    # print type(i),type(title[i])
    # os.rename(str(i),title[i])

