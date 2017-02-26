#encoding=utf-8
import jieba
import jieba.posseg as pseg
jieba.set_dictionary('dict.txt.big.txt')
# sentence = "獨立音樂需要大家一起來推廣，歡迎加入我們的行列！"
content = open('dataset/data.txt', 'rb').read()
print "Input：", content
words = pseg.cut(content)

print "Output 精確模式 Full Mode："
for word in words:
    print word.word, word.flag
