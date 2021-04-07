import re
import requests
import os
import urllib.request
import tkinter
from tkinter import *
from tkinter import messagebox
import time

date = time.asctime(time.localtime(time.time()))
date = date.replace(':','')

def cos():
    # 范围设定
    page = text

    url = 'https://api.vc.bilibili.com/link_draw/v2/Photo/list?category=cos&type=hot&page_num=' + str(page)
    url = 'https://api.vc.bilibili.com/link_draw/v2/Photo/list?category=cos&type=hot&page_num=' + str(page)
    html = requests.get(url)
    html = html.text
    # print(html)

    # 用正则表达式 筛选出图片链接
    rule = re.compile('img_src":"(.*?)","img_width')
    link = re.findall(rule, html)
    print(link)

    # 筛选图片名字
    # rule1 = re.compile('"title":"(.*?)","category')
    # name = re.findall(rule1,html)
    # print(name)

    # 时间

    # 计数
    m = 1
    # amount = float(input("下载的数量："))
    # 下载图片
    for a in link:
        # name = a.replace('/','')
        name = a.replace('https://i0.hdslb.com/bfs/album/', '')
        name = name[-4:]
        # name = a.replace('.jpg','')
        nn = str(m) + str(date) + name
        print(nn)
        # name = a.replace()
        print("正在下载%s图片" % m)
        os.makedirs('./cos/', exist_ok=True)
        urllib.request.urlretrieve(a, '.\cos\%s' % nn)
        m = m + 1
        # if m==shu:
        #     break

# 窗口
window = Tk()   #创建窗口
window.title('下载b站cos图片')  #设置窗口标题
window.geometry('300x150')   #窗口大小   用小写的x连接
window.geometry("+300+50")  #窗口位置   位置坐标前加加号
# 控件对象
# 创建一个输入框
Label(window,text = '页数').grid(row = 1,column = 2)
user_text=tkinter.Entry(window,textvariable=StringVar)
user_text.grid(row = 1,column = 3,padx = 20,pady =20)
text = user_text.get()
# Label(window,text = '数量').grid(row = 2,column = 2)
# user_text1=tkinter.Entry(window,textvariable=StringVar)
# user_text1.grid(row = 2,column = 3,padx = 20,pady =20)
# shu = user_text.get()

btn = Button(window,text = "开始",width = 10,height = 2,command = cos)
btn.grid(row = 2,column = 3,padx = 20,pady =20)

window.mainloop()   #显示窗口 消息循环
