#encoding=utf-8
import jieba
jieba.set_dictionary('dict.txt.big.txt')
# sentence = "獨立音樂需要大家一起來推廣，歡迎加入我們的行列！"
content = open('dataset/data.txt', 'rb').read()
print "Input：", content
words = jieba.cut(content, cut_all=False)
print "Output 精確模式 Full Mode："
for word in words:
    print word,

