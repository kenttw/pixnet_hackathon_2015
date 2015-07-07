import sys
import json


with open(sys.argv[1]) as json_file: # official
    benchmark = json.load(json_file)
benchmark = set((each['is_spam'],each['author']) for each in benchmark)


with open(sys.argv[2]) as json_file: # user
    predict = json.load(json_file)
predict = set((each['is_spam'],each['author']) for each in predict)


def compare(a,b):
    answer_spam = set(each for each in a if each[0] == 1)
    answer_not = a.difference(answer_spam)   
    predict_spam = set(each for each in b if each[0] == 1)
    predict_not = b.difference(predict_spam)

    tp = answer_spam.intersection(predict_spam)
    fp = predict_spam.difference(tp)
    tn = answer_not.intersection(predict_not)
    fn = predict_not.difference(tn)

    precision = float(len(tp)) / (len(tp) + len(fp)) 
    recall = float(len(tp)) / (len(tp) + len(fn)) 
    n_correct = len(a.intersection(b))
    n_total = len(a)

    print "precision is " + str(round(precision,3))
    print "recall is " + str(round(recall,3))
    print "score: %d/%d" %(n_correct,n_total)

# python score.py /path/of/the/answer /path/of/your/predict
# make sure the path's order is correct
compare(benchmark,predict)
    
