if [ ! -f "./spam.zip" ]&&[ ! -f "./spam"]; then 
   wget https://s3-ap-northeast-1.amazonaws.com/pixnet-hackathon-2015/spam/spam.zip
   unzip spam.zip
fi
if [ ! -f "./spam"]&&[ -f "./spam.zip"]; then
   unzip spam.zip
fi


