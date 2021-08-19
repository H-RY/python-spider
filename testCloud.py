import jieba     #分词
from matplotlib import pyplot as plt     #绘图，数据可视化
from wordcloud import WordCloud          #词云
from PIL import Image                    #图片处理
import numpy as np                       #矩阵运算
import sqlite3
#准备词云所需的词
conn=sqlite3.connect('movie.db')
cur=conn.cursor()
sql='select quote from doubanMovies'
data=cur.execute(sql)
text=""
for item in data:
    text=text+item[0]
cur.close()
conn.close()
#分词
cut=jieba.cut(text)
string=' '.join(cut)

img=Image.open(r'static\assets\img\circle.jpg')  #打开遮罩图片
imgArray=np.array(img)   #将图片转换为数组
wc=WordCloud(
    background_color='white',
    mask=imgArray,
    font_path="msyh.ttc",
)
wc.generate_from_text(string)

#绘制图片
fig=plt.figure(1)
plt.imshow(wc)
plt.axis('off') #是否显示坐标轴
# plt.show()  #显示生成的词云图片
plt.savefig(r'static\assets\img\word.jpg',dpi=1000)

