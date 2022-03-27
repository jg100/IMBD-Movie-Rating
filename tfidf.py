from sklearn.naive_bayes import MultinomialNB
import os
from sklearn.feature_extraction.text import TfidfVectorizer
import re

directoryPos = "./aclImdb/train/pos"
directoryNeg = "./aclImdb/train/neg"
testPos =  "./aclImdb/test/pos"
testNeg = "./aclImdb/test/neg"

tokenized_pos = []
tokenized_neg = []
corpus = []

test_y = []

def addToCorpus(path):
    # Traverse pos train folder text files
    reviewList = os.listdir(path)
    testList = reviewList[0:12500]
    for x in testList:
        if x.endswith(".txt"):
            rating = re.search(r"(?<=_)\d*", x).group()
            test_y.append(rating)

            # Open the text file
            filePath = path + "/" + x
            file = open(filePath, "r", encoding="utf8")

            # tokenize data
            text_review = file.read()
            text_review = text_review.lower()

            # remove special characters leaving only word and apostrophe
            text_review = re.sub("[^A-Za-z']+", ' ', text_review)

            corpus.append(text_review)
    return

def result(arr1, arr2):
    total = 0
    res = 0
    for x, y in zip(arr1, arr2):

        total += 1

        if x == y:
            res += 1

    print("res: ", res, ", total: ", total)

    return

addToCorpus(directoryPos)
addToCorpus(directoryNeg)

tfidf = TfidfVectorizer()

tfidf_train = tfidf.fit_transform(corpus)

MNB = MultinomialNB()
MNB.fit(tfidf_train, test_y)

# print(test_y)
# print(testResult)

corpus = []

addToCorpus(testPos)
addToCorpus(testNeg)

tfidf_test = tfidf.transform(corpus)

testResult = MNB.predict(tfidf_test)

result(test_y, testResult)