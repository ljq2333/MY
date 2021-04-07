import re
import requests
import os
import urllib.request
import time

# 范围设定
page = float(input("输入页数："))
pageshu = float(input("输入数量："))

url = 'https://api.vc.bilibili.com/link_draw/v2/Photo/list?category=cos&type=hot&page_num='+str(page)
html = requests.get(url)
html = html.text
# print(html)

# 用正则表达式 筛选出图片链接
rule = re.compile('img_src":"(.*?)","img_width')
link = re.findall(rule,html)
print(link)

# 筛选图片名字
# rule1 = re.compile('"title":"(.*?)","category')
# name = re.findall(rule1,html)
# print(name)

# 时间
time = time.asctime( time.localtime(time.time()))
print(time)
time=time.replace(':','')
# 计数
m = 1
# amount = float(input("下载的数量："))
# 下载图片
for a in link:
    # name = a.replace('/','')
    name = a.replace('https://i0.hdslb.com/bfs/album/','')
    name=name[-4:]
    # name = a.replace('.jpg','')
    nn=str(m)+time+name
    print(nn)
    # name = a.replace()
    print("正在下载%s图片"%m)
    os.makedirs('./cos/',exist_ok=True)
    urllib.request.urlretrieve(a,'.\cos\%s'%nn)
    m=m+1
    if m ==pageshu+1:
        break
