#!/usr/bin/env python
# -*- coding:utf-8 -*-
import requests
from lxml import etree
import os
import codecs
import time

baseurl = "https://foofish.net/"

basedir = r"D:\PythonCode\myblog\blog\content"
if not os.path.exists(basedir):
    os.makedirs(basedir)

content = requests.get("https://foofish.net/categories.html").content
# print content



html = etree.HTML(content)
# links = html.xpath(u"//a[text()='Python技术']/parent::*/following::*[1]//a")
# links = html.xpath(u"//a[text()='爬虫技术']/parent::*/following::*[1]//a")
# links = html.xpath(u"//a[text()='每日一题']/parent::*/following::*[1]//a")
links = html.xpath(u"//a[text()='Linux']/parent::*/following::*[1]//a")


for a in links:
    time.sleep(1)  # 等待几秒
    article_content = requests.get(a.get("href")).content
    doc = etree.HTML(article_content)

    slug = a.get("href").split("/")[-1][0:-5]

    article = doc.xpath("//article")[0]
    article.remove(article.xpath("./p[last()]")[0])
    content = etree.tostring(article)

    title = doc.xpath("//h1[@class='header-title']")[0].text
    summary = doc.xpath("//meta[@name='description']")[0].get("content")
    author = doc.xpath("//p[@class='header-date']/a")[0].text
    category = doc.xpath("//p[@class='header-date']/a")[1].text
    date = doc.xpath("//p[@class='header-date']/a")[0].tail.split(",")[1]
    tags = list(map(lambda x: x.text, doc.xpath("//p[@class='pull-right header-tags']/a")))

    category_folder = os.path.join(basedir, category)
    if not os.path.exists(category_folder):
        os.makedirs(category_folder)
    with codecs.open(os.path.join(category_folder, slug + ".md"), "w+", encoding="utf-8") as f:
        s = '''Title: %s
Date: %s
Category: %s
Tags: %s
Slug: %s
Author: Alex
Summary: %s

%s

Original:%s
        ''' % (title, date, category, ",".join(tags), slug, summary, content, a.get("href"))
        f.write(s)
        print title


        for img in article.xpath(".//img[starts-with(@src,'../images/')]"):
            img_content = requests.get(baseurl+img.get("src")[3:]).content
            img_filename = img.get("src")[3:]  # sub ../images/
            img_filename = os.path.join(basedir,  img_filename).replace("/","\\")
            img_dir2=os.path.split(img_filename)[0]
            if not os.path.exists(img_dir2):
                os.makedirs(img_dir2)
            with open(img_filename, "wb") as f:
                f.write(img_content)
            print img_filename
