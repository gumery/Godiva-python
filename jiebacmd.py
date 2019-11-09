#encoding=utf-8
#usage example (find top 100 words in abc.txt):
#用途：找出abc.txt文件中出现频率最高的前100个词
#复制以下命令到cygwin里运行，abc.txt是你文本的文件名，head -100可以自己改成想要提取的前多少个词
#cat abc.txt | python jiebacmd.py | sort | uniq -c | sort -nr -k1 | head -100
#以上都是注释，不影响程序运行
from __future__ import unicode_literals
import sys
sys.path.append("../")
reload(sys)
sys.setdefaultencoding( "utf-8" )
import jieba
default_encoding='utf-8'
if len(sys.argv)>1:
    default_encoding = sys.argv[1]
while True:
    line = sys.stdin.readline()
    if line=="":
        break
    line = line.strip()
    for word in jieba.cut(line):
        print(word)
