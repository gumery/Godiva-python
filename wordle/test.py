#!/usr/bin/env python
# -*- coding:utf-

import matplotlib                                                                                                         
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import jieba
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import jieba.analyse
import io
from collections import Counter

#data = io.open('/home/ubuntu/data.txt',encoding='utf-8').read()
#tag=jieba.analyse.extract_tags(data,120)
#print(tag)
#c=Counter()
#for x in tag:
#    if len(x)>1 and x != '\r\n':
#        c[x] += 1

#print('\n词频统计结果：')
#for (k,v) in c.most_common(120):# 输出词频最高的前两个词
#    print("%s:%d"%(k,v))
    

from wordcloud import WordCloud

txt1 = io.open('/home/ubuntu/data.txt', 'r', encoding='utf8').read()    # txt文件，随便放点中文文章
words_ls = jieba.cut(txt1, cut_all=True)
words_split = " ".join(words_ls)

wc = WordCloud(font_path='/home/ubuntu/simhei.ttf',background_color='White')    # 一定要设（）内这个参数。否则会显示一堆小方框简化版：font_path="simhei.ttf"，默认黑色背景
my_wordcloud = wc.generate(words_split)
plt.imshow(my_wordcloud,interpolation="bilinear")
plt.axis("off")
plt.show()

wc.to_file('wordcloud.png') # 保存图片文件
