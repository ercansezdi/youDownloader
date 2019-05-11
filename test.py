from pytube import YouTube
indirme_link = "https://www.youtube.com/watch?v=HirFutbbIWg&list=RDHirFutbbIWg&start_radio=1"

baglan = YouTube(indirme_link)
baslik = baglan.streams.all()
quatlity = []
for i in baslik:
   if str(i).find("mp4",17) != -1:
      k = str(i).split('res="')
      try:
         if k[1][3].isnumeric() and k[1][0].isnumeric():
            cozunurluk = k[1][0] + k[1][1] + k[1][2] + k[1][3]

            if not(cozunurluk in quatlity) and cozunurluk != "Non":
               quatlity.append(cozunurluk)
         else:
            cozunurluk = k[1][0] + k[1][1] + k[1][2]

            if not(cozunurluk in quatlity) and cozunurluk != "Non":
               quatlity.append(cozunurluk)
      except:
         pass
print(quatlity)