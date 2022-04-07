from sklearn.naive_bayes import MultinomialNB
import os
from sklearn.feature_extraction.text import TfidfVectorizer
import re

directoryPos = "./aclImdb/train/pos"
directoryNeg = "./aclImdb/train/neg"
testPosDirectory =  "./aclImdb/test/pos"
testNegDirectory = "./aclImdb/test/neg"

corpus = []

review_actual_val = []

def addToCorpus(path, reviewName):
    # Traverse pos train folder text files
    
    for x in reviewName:
        if x.endswith(".txt"):
            rating = re.search(r"(?<=_)\d*", x).group()
            review_actual_val.append(rating)

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

def test(mnb, testPos, testNeg, firstIndex, lastIndex):
    global corpus
    corpus = []
    global review_actual_val
    review_actual_val = []

    posReviewName = os.listdir(testPos)[firstIndex: lastIndex]
    addToCorpus(testPos, posReviewName)
    negReviewName = os.listdir(testNeg)[firstIndex: lastIndex]
    addToCorpus(testNeg, negReviewName)

    tfidf_test = tfidf.transform(corpus)
    testResult = mnb.predict(tfidf_test)

    result(review_actual_val, testResult)
    return

posReviewName = os.listdir(directoryPos)[0:2000]
addToCorpus(directoryPos, posReviewName)
negReviewName = os.listdir(directoryNeg)[0:2000]
addToCorpus(directoryNeg, negReviewName)

tfidf = TfidfVectorizer()

tfidf_train = tfidf.fit_transform(corpus)

MNB = MultinomialNB(alpha = 1)

MNB.fit(tfidf_train, review_actual_val)

test(MNB, testPosDirectory, testNegDirectory, 0, 1000)
test(MNB, testPosDirectory, testNegDirectory, 1000, 2000)
test(MNB, testPosDirectory, testNegDirectory, 2000, 3000)
test(MNB, testPosDirectory, testNegDirectory, 3000, 4000)
test(MNB, testPosDirectory, testNegDirectory, 4000, 5000)