# import wx
# app = wx.App()
# frame = wx.Frame(None, title='hello wxPython')  # 创建窗口
# frame.Show()
# app.MainLoop()
import os,sys,time
def jiancha():
    z=-1
    txt = 'pip-review'
    li = os.popen(txt).read()
    print(li)
    f = str(input('是否开始更新[请输入OK]:'))
    if f==str('OK') :
        print('现在开始')
        time.sleep(1)
    else:
        sys.exit()
    li = li.split('\n')

    for a in li:
        m= a.find('=')
        z=z+1
        li[z]=a[:m]
        d = os.popen('pip install --upgrade %s' % li[z]).read()
        print(d)

    # d = os.popen('pip install --upgrade %s' % li).read()
    # print(d)

jiancha()