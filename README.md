# Chatbot

# 利用wikidata.py處理wiki資料
	step1. 先去下載wiki data(https://zh.wikipedia.org/wiki/Wikipedia:数据库下载)
		   選擇中文下載，進去後選擇最近日期，選擇長得像這樣的檔案zhwiki-20170220-pages-articles.xml.bz2(日期可能不同)

	step2. 載完後install gensim:
		   pip3 install --upgrade gensim
		   python3 wikidata.py zhwiki-20170220-pages-articles.xml.bz2

# 產出的wiki_texts.txt因為會繁簡夾雜所以須使用opencc簡轉繁

	step1. mac install opencc(記得要先灌Doxygen，不然會出現錯誤訊息)
		(1)download opencc
		(2)打開terminal到download的file中
		(3)terminal打上:
			make PREFIX=/usr/local
			sudo make PREFIX=/usr/local install

	step2. 使用opencc簡轉繁：在terminal打上：
			opencc -i wiki_texts.txt -o wiki_zh_tw.txt -c s2t.json

# 利用結巴斷詞
python 
