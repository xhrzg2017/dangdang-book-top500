#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @编辑器        : PyCharm 
# @项目名        : 当当网
# @文件名        : demo.py
# @作者          : xhrzg2017 
# @邮箱          : xhrzg2017@gmail.com
# @团队          : 广州电脑初哥工作室
# @创建时间       : 2021/4/22 18:05 
# @Editor       : PyCharm 
# @Project_Name : 当当网
# @File_Name    : demo.py
# @Author       : xhrzg2017 
# @Email        : xhrzg2017@gmail.com
# @Team         : Guangzhou computer novice studio
# @Time         : 2021/4/22 18:05


import requests
import parsel
import csv

f = open('book.csv', mode='a', encoding='utf-8-sig', newline='')
csv_writer = csv.DictWriter(f, fieldnames=['标题', '评论量', '推荐值', '作者', '出版日期', '出版社', '原价', '售价', '折扣', '电子书价格', '详情页地址'])
csv_writer.writeheader()  #
for page in range(1, 26):
    print('=' * 10 + f'正在爬取第{page}页' + '=' * 10)
    # 发送请求头
    url = f'http://bang.dangdang.com/books/bestsellers/01.41.00.00.00.00-year-2020-0-1-{page}'
    # 伪装浏览器UA
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.72 Safari/537.36 Edg/90.0.818.42'
    }
    response = requests.get(url=url, headers=headers)
    # 自动转码
    response.encoding = response.apparent_encoding
    # 获取网页数据
    # print(response.text)
    # 解析数据  提取我们需要的内容 re正则表达式 css xpath
    selector = parsel.Selector(response.text)
    # css选择器 根据标签 属性提取数据内容
    # 分两次提取 <li>列表
    lis = selector.css('ul.bang_list li')
    for li in lis:
        title = li.css('.name a::text').get()  # 标题
        comment = li.css('.star a::text').get()  # 评论量
        recommend = li.css('span.tuijian::text').get()  # 推荐值
        author = li.css('div:nth-child(5) a:nth-child(1)::attr(title)').get()  # 作者
        publicationDate = li.css('div:nth-child(6) span::text').get()  # 出版日期
        press = li.css('div:nth-child(6) a::text').get()  # 出版社
        price_r = li.css('.price .price_r::text').get()  # 原价
        price_n = li.css('.price p:nth-child(1) .price_n::text').get()  # 售价
        price_s = li.css('.price .price_s::text').get()  # 折扣
        price_e = li.css('.price .price_e .price_n::text').get()  # 电子书
        href = li.css('.name a::attr(href)').get()  # 链接
        dit = {
            '标题': title,
            '评论量': comment,
            '推荐值': recommend,
            '作者': author,
            '出版日期': publicationDate,
            '出版社': press,
            '原价': price_r,
            '售价': price_n,
            '折扣': price_s,
            '电子书价格': price_e,
            '详情页地址': href,
        }
        csv_writer.writerow(dit)
        # print(title, comment, recommend, author, publicationDate, press, price_r, price_n, price_s,price_e, href, sep='|')
