from tkinter import *
from pytube import YouTube
from threading import Thread
import os

class downloader(Frame):
    def __init__(self,parent):
        Frame.__init__(self,parent)
        self.parent = parent
        #self.parent.attributes("-fullscreen", True) # fullscreen
        self.frame_1 = Frame(self.parent)
        self.frame_1.grid(row=0,column=0)
        self.frame_2 = Frame(self.parent)
        self.frame_radioButton = Frame(self.frame_2)
        self.frame_radioButton.grid(row=7, column=0, columnspan=3, rowspan=1, padx=0, pady=5)
        self.parent.geometry('900x700')
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
        self.var = IntVar()
        self.sart = False
        self.ekran()

    def ekran(self):
        #################################### Entry ####################################
        self.giris = Entry(self.frame_1,bg=self.backGround, bd=5, font=self.yaziTipiText, width=52)
        self.giris.grid(row=1, column=0, columnspan=3, rowspan=1, padx=5, pady=5)
        self.adres = Entry(self.frame_2,bg = self.backGround, bd = 5, font = self.yaziTipiText, width = 40)
        self.adres.grid(row=6, column=0, columnspan=3, rowspan=1, padx=0, pady=5)

        #################################### Button ####################################
        #self.button1.grid(row=4, column=1, columnspan=1, rowspan=1, padx=1, pady=30)

        self.button2 = Button(self.frame_1,text='Kapat', font=self.yaziTipi, bg=self.backGround, wraplength=500, height=1, bd=2,
                              width=8, command=self.parent.destroy)
        self.button2.grid(row=4, column=0, columnspan=1, rowspan=1, padx=2, pady=30)
        self.button3 = Button(self.frame_1,text='Link Doğrula', font=self.yaziTipi, bg=self.backGround, wraplength=500, height=1, bd=2,
                              width=9, command=self.on_dogrula)
        self.button3.grid(row=4, column=2, columnspan=1, rowspan=1, padx=0, pady=30)
        self.button4 = Button(self.frame_2, text='İndirmeyi Başlat', font=self.yaziTipi, bg=self.backGround, wraplength=500,
                              height=1, bd=2, width=12, command=self.on_baslat)
        self.button4.grid(row=8, column=0, columnspan=3, rowspan=1, padx=0, pady=5)
        #################################### Label ####################################
        self.text1 = Label(self.frame_1,text='Lütfen indirme linkini giriniz.', font=self.yaziTipi, bg=self.backGround,
                           wraplength=523, anchor='center', width=35)  # ok
        self.text1.grid(row=0, column=0, sticky=W, padx=0, pady=0, columnspan=3, rowspan=1)
        self.text2 = Label(self.frame_2, text='Kaydetme Adresi giriniz.', font=self.yaziTipi, bg=self.backGround,
                           wraplength=523, anchor='center', width=35)  # ok
        self.text2.grid(row=0, column=0, sticky=W, padx=0, pady=0, columnspan=3, rowspan=1)
        self.text2= Label(self.frame_1,textvariable = self.textVar,font =self.yaziTipi,bg = self.backGround,
                          wraplength=523,anchor = 'center',width = 35)
        self.text2.grid(row=5,column=0,sticky=W, padx=0 ,  pady = 30,columnspan=3,rowspan=1)
        self.textVar.set('@auther Ercan Sezdi')
        ################################### Listbox ####################################

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

            #self.link = self.giris.get()
            self.link = "https://www.youtube.com/watch?v=BxuY9FET9Y4"
            if self.link != '':
                self.baglan = YouTube(self.link)
                baslik = self.baglan.streams.all()
                self.quatlity = []
                for i in baslik:
                    if str(i).find("mp4", 17) != -1:
                        k = str(i).split('res="')
                        try:
                            if k[1][3].isnumeric() and k[1][0].isnumeric():
                                cozunurluk = k[1][0] + k[1][1] + k[1][2] + k[1][3]
                                if cozunurluk != "Non":
                                    if not(int(cozunurluk) in self.quatlity):
                                        self.quatlity.append(int(cozunurluk))
                            else:
                                cozunurluk = k[1][0] + k[1][1] + k[1][2]
                                if cozunurluk != "Non":
                                    if not(int(cozunurluk) in self.quatlity) and cozunurluk != "Non":
                                        self.quatlity.append(int(cozunurluk))
                        except:
                            pass
                self.sart = True
                self.quatlity.sort()
                if len(self.quatlity) > 0:
                    self.R1 = Radiobutton(self.frame_radioButton, text=self.quatlity[0], variable=self.var, value=int(self.quatlity[0]),
                                     command=self.ayar)
                    self.R1.grid(row=0,column=0)
                if len(self.quatlity) > 1:
                    self.R2 = Radiobutton(self.frame_radioButton, text=self.quatlity[1], variable=self.var, value=int(self.quatlity[1]),
                                     command=self.ayar)
                    self.R2.grid(row=0, column=1)
                if len(self.quatlity) > 2:
                    self.R3 = Radiobutton(self.frame_radioButton, text=self.quatlity[2], variable=self.var, value=int(self.quatlity[2]),
                                     command=self.ayar)
                    self.R3.grid(row=0, column=2)
                if len(self.quatlity) > 3:
                    self.R4 = Radiobutton(self.frame_radioButton, text=self.quatlity[3], variable=self.var, value=int(self.quatlity[3]),
                                     command=self.ayar)
                    self.R4.grid(row=0, column=3)
                if len(self.quatlity) > 4:
                    self.R5 = Radiobutton(self.frame_radioButton, text=self.quatlity[4], variable=self.var, value=int(self.quatlity[4]),
                                     command=self.ayar)
                    self.R5.grid(row=0, column=4)
                if len(self.quatlity) > 5:
                    self.R6 = Radiobutton(self.frame_radioButton, text=self.quatlity[5], variable=self.var, value=int(self.quatlity[5]),
                                     command=self.ayar)
                    self.R6.grid(row=0, column=5)
            else:
                self.textVar.set('Linki boş bırakma')
        except :
            self.textVar.set('Linkin hatalı')
        if self.sart:
            self.sart = False

            self.indir()
    def ayar(self):
        self.quatlity_cozunurluk = self.var.get()
        print("XX",self.quatlity_cozunurluk)
    def baslat(self):
        print("YY",self.quatlity_cozunurluk)
        self.link = "https://www.youtube.com/watch?v=BxuY9FET9Y4"
        self.baglan = YouTube(self.link)
        self.indirme_link = self.baglan.streams.first()
        self.indirme_link.download()#self.kayit_adres
        self.frame_2.grid_remove()
        self.frame_1.grid(row=0, column=0)

    def ara_baslat(self):
        self.adres.grid_remove()
        self.button4.grid_remove()
        self.baslat()

    def on_baslat(self):

        try:
            #self.kayit_adres = self.adres.get()
            self.kayit_adres ="C:\\Users\\trfrever\\Desktop\\project\\youtube_downloader"
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
        self.frame_1.grid_remove()
        self.frame_2.grid(row=0,column=0)
        self.textVar.set('Kaydetme adresi giriniz.')


if __name__ == "__main__":
    tk = Tk()
    basla = downloader(tk)
    tk.mainloop()
