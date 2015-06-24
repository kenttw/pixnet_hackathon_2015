if [ ! -f new.dict_all ]; then
	wget https://github.com/texib/chinese_terms/raw/master/new.dict_all
fi
if [ ! -f stopword.txt ]; then
	wget https://raw.githubusercontent.com/texib/chinese_terms/master/stopword.txt
fi