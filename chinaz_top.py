#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
爬取站长之家 中文排行榜域名
起始链接:https://top.chinaz.com/all/index.html
分页链接:https://top.chinaz.com/all/index_2.html
By:Black_list
'''

import requests
import re

url = 'https://top.chinaz.com/all/'
def black(url):
    blacklist = [
        #只能匹配一级后缀   无法匹配 .com.cn 二级后缀 懒得匹配了
        '163.com',
        'qq.com',
        'gov.cn',
        'baidu.com',
        'sohu.com',
        'weibo.com',
        'douban.com',
        'iqiyi.com',
        'ifeng.com',
        'sogou.com',
        'youku.com',
        'so.com',
        'taobao.com',
        'apple.com',
        '58.com',
        'jd.com',
        'chinaz.com',
        '1688.com'
    ]
    url = url.split('.')
    url = url[-2]+'.'+url[-1]
    for j in blacklist:
            if url == j:
                return True
def pachong(url):
    try:
        html = requests.get(url)
        url_regular = 'class="col-gray">(.*?)</span>'
        if html.status_code == 200:
            res_url = re.findall(url_regular,html.text)
            del res_url[0]
            for urls in res_url:
                if black(urls) == True:
                    print('黑名单域名已过滤')
                else:
                    print(urls)
                    with open('top_url.txt','a+') as f:
                        f.write(urls)
                        f.write('\n')
                        f.close()
        else:
            '链接访问错误！'
    except BaseException as e:
        pachong(url)


def fenye(res_url):
    pachong(res_url)
    i = 2
    while True:
        url = res_url + 'index_%d.html' % i
        i = i+1
        if i == 1922:
            print('域名采集结束')
            break
        else:
            pachong(url)

fenye(url)


