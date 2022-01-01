import wx,re,os

class MyFrame(wx.Frame):
    def __init__(self,parent,id):
        title1 = r""
        wx.Frame.__init__(self,parent,id,title = "vb",size=(750,400))
        panel = wx.Panel(self)
        # panel.Bind(wx.EVT_KEY_DOWN,self.onkeydown)
        # self.Bind(wx.EVT_KEY_DOWN,self.onkeydown)
        # self.Centre()
        # self.Show(True)

        self.title1 = wx.StaticText(panel,label= "输入",pos = (140,20))
        # self.title2 = wx.StaticText(panel,label= "输出",pos = (500,20))

        self.text_1 = wx.TextCtrl(panel,pos=(20,50),size= (300,300),style = wx.TE_MULTILINE)
        # self.text_2 = wx.TextCtrl(panel,pos=(400,50),size= (300,300),style = wx.TE_MULTILINE)

        self.bt2 = wx.Button(panel, label='运行', pos=(330, 50), size=(100, 50))
        self.bt2.Bind(wx.EVT_BUTTON, self.ontitle)
        self.bt1 = wx.Button(panel,label= 'msgbox',pos = (330,100),size = (100,50))
        self.bt1.Bind(wx.EVT_BUTTON, self.onmsgbox)
        self.bt6 = wx.Button(panel,label="for",pos=(330,150),size=(100,50))
        self.bt6.Bind(wx.EVT_BUTTON,self.for1)
        self.bt4 = wx.Button(panel,label = "if",pos =(330,200),size = (100,50))
        self.bt4.Bind(wx.EVT_BUTTON, self.if1)
        self.bt5 = wx.Button(panel,label="select",pos=(330,250),size=(100,50))
        self.bt5.Bind(wx.EVT_BUTTON,self.select1)
        self.bt4 = wx.Button(panel, label="清空", pos=(330, 300),size = (100,50))

        self.bt4.Bind(wx.EVT_BUTTON, self.qink)
        self.bt3 = wx.Button(panel, label="删除", pos=(640, 0))
        self.bt3.Bind(wx.EVT_BUTTON, self.cls)


    def for1(self,event):
       self.text_1.write("for \n    \n next")
       self.text_1.SetFocus()
    def qink(self,event):
        self.text_1.ChangeValue("")
        self.text_1.SetFocus()
    def select1(self,event):
        self.text_1.write("select case \n     \nend select ")
        self.text_1.SetFocus()
    def if1(self,event):
        self.text_1.write(r"if  then  ")
        self.text_1.SetFocus()
    def cls(self,event):
        os.remove(r"vbse.vbs")
        self.Close(True)
    def onmsgbox(self,event):
        title2 = r"msgbox "
        self.text_1.write(title2)
        self.text_1.SetFocus()
    def ontitle(self,event):

        title2 = self.text_1.GetValue()
        file1 = open(r"vbse.vbs","w+",encoding = "utf-8")
        file1.write(title2)
        file1.fileno()
        #os.rename(r"C:\Users\ljq23\Desktop\vbse.txt",r"C:\Users\ljq23\Desktop\vbse.vbs")
        #os.system(r"vbse.vbs")
        os.popen(r"vbse.vbs")


if __name__ == "__main__":
    app = wx.App()
    frame = MyFrame(parent=None,id = -1)
    frame.Show()
    app.MainLoop()
