import requests,urllib.request
import os
import re

uid = str(input('uid:'))
amount = str(input('页数：'))
uid_url = 'http://photo.weibo.com/photos/get_all?uid=' + uid +'&album_id=4321786105700265&count=30&page=' + amount + '&type=3'

class weibotu:

    def __init__(self,url):         #cookies与获取相册图页内容
        cookies ={'Cookie':'SINAGLOBAL=2446604562194.155.1546166933167; un=liujiaqing1016@163.com; wvr=6; UOR=,,www.moe123.net; ALF=1577711278; SSOLoginState=1546175280; SCF=An8InabEGO_lqs6khKLaa7VsOJJOiX32x2hE8S67rVPtbEqjOD_BiHnfFy1nMDsusRfC-fHXnFXHv_i21o-K3aE.; SUB=_2A25xLLNlDeRhGeBM7VoQ8ynMyDuIHXVSW6OtrDV8PUNbmtANLWnRkW9NRNiUyV0CeCJJe8Fybk4wnZjnX6zJDOby; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WhhDiRTTocLFBgHZrhDooxA5JpX5KzhUgL.FoqESonpe0M7e0M2dJLoI0YLxKqLB.zL1K2LxKMLBKnLB.BLxKqLBK5L1K2LxKBLBonL12zLxKML1-2L1hBLxKML1h.LBK.LxKnLB-qLB-Bt; SUHB=0laVV6LhwHukV5; _s_tentry=weibo.com; Apache=3634444741317.9126.1546175479127; ULV=1546175479136:2:2:2:3634444741317.9126.1546175479127:1546166933176'
                  }

        # url = 'http://photo.weibo.com/photos/get_all?uid=6409538840&album_id=4321786105700265&count=30&page=1&type=3&__rnd=1545919565501'
        html = requests.get(url,cookies=cookies)
        html.encoding = 'utf-8'
        self.html = html.text
        print(self.html)

    def url_er(self):           #分割内容
        url_name_re = re.compile('pic_name":"(.*?)","pic_pid":"(.*?)","pic_type":1,"source":"","tags":"","timestamp":(.*?),"uid":(.*?)')
        url_name = re.findall(url_name_re,self.html)
        self.url_name = url_name
        print(url_name)

    def download(self):         #下载图片和拼合链接
        m = 1
        for i in self.url_name:
            link = i[0]
            name = i[1]
            link_url = 'http://wx4.sinaimg.cn/large/'+link
            # print(link)
            # print(name)

            print("正在下载%s图片" % name)
            print('第%s'%m)
            os.makedirs('./weibotu/', exist_ok=True)
            urllib.request.urlretrieve(link_url, '.\weibotu\%s' % link)
            m = m+1



weibotu = weibotu(uid_url)
weibotu.url_er()
weibotu.download()

