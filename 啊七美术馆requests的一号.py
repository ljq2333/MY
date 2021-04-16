import requests,re,time,os
# html='https://a7a7.net/meitu/index.php/archives/559/'
url = str(input("输入a7a7.net链接："))
headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36 Edg/84.0.522.40"
}
proxies = {
    "http":"127.0.0.1:7890",
    "https":"127.0.0.1:7890"
}
ht = requests.get(url,headers = headers,verify = False,proxies = proxies,timeout = 10)
ht=ht.text
# print(ht)
ht_tit = re.findall('<title>(.*?)</title>',ht)
ht_re = '<img class="(.*?)" src="(.*?)" data-original="(.*?)" alt="(.*?)"'
ht_us = re.findall(ht_re,ht)
print(ht_tit)
os.mkdir('./ %s' % ht_tit[0])
for item in ht_us:
    tp_url = item[2]
    tp_na = item[3] +tp_url[-5:]
    # print(tp_url,tp_na)
    tp = requests.get(tp_url,headers = headers,verify = False,proxies = proxies,timeout = 5)
    tp_pt = '.\ '+ht_tit[0]+r'\\'+tp_na
    print(tp_na)
    open('%s'%tp_pt, 'wb').write(tp.content)
    time.sleep(0.2)