from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
from scipy.misc import imread
import matplotlib.pyplot as plt
import random
import os
from os import path

d="C:\\Users\\Ozgur\\Desktop\\otivit\\kitaplar\\txt2"
for root, dirs, files in os.walk("C:\\Users\\Ozgur\\Desktop\\otivit\\kitaplar\\txt2"):
    for file in files:
        if file.endswith('.txt'):
         print(file)
         text=""
         text = open(path.join(d, file)).read()
         text=text.replace("İ", "i")
         text=text.replace("Ğ", "ğ")
         text=text.replace (chr(34)," ")
         text=text.replace (chr(8212)," ")
         text=text.replace (chr(8226)," ")
           
         
         ztop=['de','da','ve','bir','ki','bu', 'nin','dedi', 'mi','diye','mı','ile','için','gibi','her','kadar','ne','ya','en','of','iki',
               'şey','göre','ama','olarak','onun','bunun','değil','sonra','daha','veya','bile','nın','ii','böylece','yalnızca','ancak','ın','un',
               'fakat','çünkü','ise','dnce','yı','nm','ona','onu','neden','ben','vardı','başka','mu','artık','hep','hiç','beni','var','sen','o',
               'biz','siz','onlar','işte','sanki','yoksa','önce','çok','bunu','dedim','olduğunu','olduğu','olan','hemen','nasıl','hem','size','beni',
               'bana','seni','sana','bizi','onları','benden','senden','bize','bizden','bi','öyle','biraz','biri','herhalde','şu','o','zaten','etti',
               'kendi','kendine','kendisi','tüm','hiçbir','tarafından','sadece','diğer','yoktu','yok','dediydi','demişti','bütün','benim','içinde','üzerinde',
               'üstünde','senin','bizim','onların','şeyi','verdi','hatta','kim','pek','böyle','değildi','şimdi','zaman','üç','dört','beş','idi','ederim',
               'sizi','onlara','onlardan','ondan','onda','değildir','da','arasında','kere','nerde','oldu','ettim','ettiler','burda','burada','orda','orada','şurda',
               'şurada','hatta','onunla','benimle','seninle','bizimle','sizinle','onlarla','kendini','birkaç','şekilde','kendisine','belki','eğer','içine','üzerine',
               'ertesi','gün','evet','bunları','bunlara','bunlardan','şunları','onları','kendisini','sizin','iyi','aynı','yine','kendimi','kez','başladı','acaba',
               'gene','hayır','musun','mi','misin','kaç','niye','buna','gerçekten','bugün','yarın','gece','diyor','doğru','iyice','üstüne','doğru',
               'arkasından','olur','olsun','önüne','yanına','yere','in']
         '''liste2=[]   
         ekle=text.split()
         for x in ekle:
          x.strip('.,-;:!?')
          x.rstrip()
          x=x.lower()
          if x.endswith("du") or x.endswith("dü") or x.endswith("di") or x.endswith("dı") :
            if x not in ztop:
             ztop.append(x)
             liste2.append(x)       
         #print(liste2)'''        
         wordcloud = WordCloud(background_color='whitesmoke',  max_words=50, max_font_size=90, relative_scaling=1.0 ,
                      stopwords = ztop # set or space-separated string
                      ).generate(text.lower())

         default_colors = wordcloud.to_array()	
         plt.imshow(wordcloud, interpolation="bilinear")
         plt.axis("off")
         #plt.show()
         file=file.replace(".txt"," ")
         plt.savefig("C:\\Users\\Ozgur\\Desktop\\otivit\\kitaplar\\grafik2\\"+file+".png")
