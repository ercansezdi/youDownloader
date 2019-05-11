from tkinter import *
from pytube import YouTube
from threading import Thread
import os

class downloader(Frame):
    def __init__(self,parent):
        Frame.__init__(self,parent)
        self.parent = parent
        self.parent.attributes("-fullscreen", True) # fullscreen
        #self.parent.geometry('700x700')
        self.parent.bind('<Escape>',quit)
        self.arkaPlanRenk = 'white'
        self.backGround = 'white'
        self.yaziRengi = 'blue'
        self.yaziTipi = "Helvetica 20 bold italic"
        self.yaziTipiText = "Helvetica 12 bold italic"
        # delete
        self.kaydetme_adres = "C:\\Users\\trfrever\\Desktop\\project\\youtube_downloader"
        self.indirme_link = ""

        self.parent.configure(background=self.arkaPlanRenk)#,cursor = 'none')
        self.textVar = StringVar()
        self.sart = False
        self.ekran()

    def ekran(self):
        #################################### Entry ####################################
        self.giris = Entry(bg=self.backGround, bd=5, font=self.yaziTipiText, width=52)
        self.giris.grid(row=1, column=0, columnspan=3, rowspan=1, padx=5, pady=5)

        #################################### Button ####################################
        #self.button1 = Button(text='Link Doğrula', font=self.yaziTipi, bg=self.backGround, wraplength=500, bd=2,
        #                      height=1, width=11, command=self.on_dogrula)
        #self.button1.grid(row=4, column=1, columnspan=1, rowspan=1, padx=1, pady=30)

        self.button2 = Button(text='Kapat', font=self.yaziTipi, bg=self.backGround, wraplength=500, height=1, bd=2,
                              width=8, command=self.parent.destroy)
        self.button2.grid(row=4, column=0, columnspan=1, rowspan=1, padx=2, pady=30)
        self.button3 = Button(text='İndir', font=self.yaziTipi, bg=self.backGround, wraplength=500, height=1, bd=2,
                              width=9, command=self.on_dogrula)
        self.button3.grid(row=4, column=2, columnspan=1, rowspan=1, padx=0, pady=30)

        #################################### Label ####################################
        self.text1 = Label(text='Lütfen indirme linkini giriniz.', font=self.yaziTipi, bg=self.backGround,
                           wraplength=523, anchor='center', width=35)  # ok
        self.text1.grid(row=0, column=0, sticky=W, padx=0, pady=0, columnspan=3, rowspan=1)
        self.text2= Label(textvariable = self.textVar,font =self.yaziTipi,bg = self.backGround,
                          wraplength=523,anchor = 'center',width = 35)
        self.text2.grid(row=5,column=0,sticky=W, padx=0 ,  pady = 30,columnspan=3,rowspan=1)
        self.textVar.set('@auther Ercan Sezdi')

    def on_dogrula(self):
        yazilar = Thread(target=self.yazi,args = (True,))
        dogrulama = Thread(target=self.dogrula)
        dogrulama.start()
        yazilar.start()

    def yazi(self,value):
        if value == True :
            self.textVar.set('Link Doğrulanıyor...')
        else:
            self.textVar.set('indiriliyor...')

    def dogrula(self):
        try:
            self.link = self.giris.get()
            if self.link != '':
                self.baglan = YouTube(self.link)
                self.sart = True
            else:
                self.textVar.set('Linki boş bırakma')
        except :
            self.textVar.set('Linkin hatalı')
        if self.sart:
            self.sart = False
            self.baslat()

    def baslat(self):

        self.indirme_link = self.baglan.streams.first()
        self.indirme_link.download()#self.kayit_adres
        self.textVar.set('İndirme Tamamlandı.')

    def ara_baslat(self):
        self.adres.grid_remove()
        self.button4.grid_remove()
        self.baslat()

    def on_baslat(self):

        try:
            self.kayit_adres = self.adres.get()
            if self.kayit_adres != '':
                if not(os.path.exists(self.kayit_adres)):
                    self.textVar.set('Adres hatalı')
                else:
                    yazilar = Thread(target=self.yazi,args = (False,))
                    dogrulama = Thread(target=self.ara_baslat)
                    dogrulama.start()
                    yazilar.start()
            else:
                self.textVar.set('Adresi boş bırakma')

        except:
            self.textVar.set('Adres hatalı')

    def indir(self):
        if self.sart == True:
            self.textVar.set('Kaydetme adresi giriniz.')

            self.adres = Entry(bg = self.backGround,bd = 5, font = self.yaziTipiText,width =40)
            self.adres.grid(row=6,column=0,columnspan = 3,rowspan = 1,padx=0,pady=5)

            self.button4 = Button(text = 'Başlat',font =self.yaziTipi,bg = self.backGround,wraplength=500, height = 1,bd = 2, width = 9, command = self.on_baslat)
            self.button4.grid(row=7,column=0,columnspan=3,rowspan = 1,padx=0,pady=5)

if __name__ == "__main__":
    tk = Tk()
    basla = downloader(tk)
    tk.mainloop()
