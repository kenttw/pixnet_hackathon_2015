# pixnet_hackathon_2015
pixnet_hackathon_2015
# chinese_terms

# spam detection
- __Performance evaluation.__ We provide score.py to evaluate the performance of your prediction.
- __Format.__ score.py is able to process data in the following json format:
```json
[
    {
        "author": "author_id",
        "is_spam": 1
    },
    {
        "author": "author_id",
        "is_spam": 0
    },
    {
        "author": "author_id",
        "is_spam": 0
    }
]
```
- __Example.__ Please make sure the order of the path is correct. (standard answer / your answer)
```
>>> python score.py /path/of/the/answer.json /path/of/your/predict.json
```
```
precision is 0.985
recall is 0.996
accuracy: 259/264 (correct/total)
```
