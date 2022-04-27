import os
import re

directoryPos = "./aclImdb/train/pos"
directoryNeg = "./aclImdb/train/neg"
testPosDirectory =  "./aclImdb/test/pos"
testNegDirectory = "./aclImdb/test/neg"

corpus = []
review_actual_val = []

# stop list from nltk
stopwords = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself", 
            "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", 
            "itself", "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", 
            "that", "these", "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", 
            "had", "having", "do", "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", 
            "because", "as", "until", "while", "of", "at", "by", "for", "with", "about", "against", "between", 
            "into", "through", "during", "before", "after", "above", "below", "to", "from", "up", "down", "in", 
            "out", "on", "off", "over", "under", "again", "further", "then", "once", "here", "there", "when", 
            "where", "why", "how", "all", "any", "both", "each", "few", "more", "most", "other", "some", "such", 
            "no", "nor", "not", "only", "own", "same", "so", "than", "too", "very", "s", "t", "can", "will", 
            "just", "don", "should", "now"]

# Get reviews from a folder
# store the text in the corpus and store vals in a array also 
def getReviews(path, firstIndex, lastIndex):
    corpus = []
    review_actual_val = []

    # Traverse folder for text files names
    reviewNames = os.listdir(path)[firstIndex:lastIndex]
    
    for x in reviewNames:
        if x.endswith(".txt"):
            rating = re.search(r"(?<=_)\d*", x).group()
            review_actual_val.append(rating)

            # Open the text file
            filePath = path + "/" + x
            file = open(filePath, "r", encoding="utf8")

            # add review to corpus
            text_review = file.read()
            corpus.append(text_review)
    return corpus, review_actual_val

            # text_review = text_review.lower()

            # # remove special characters leaving only word and apostrophe
            # text_review = re.sub("[^A-Za-z']+", ' ', text_review)

def filterData(corpus, stopwords):
    tempCorpus = []
    for text_review in corpus:
        
        # turn every character to lower case
        text_review = text_review.lower()
        
        # specific
        text_review = re.sub(r"won\'t", "will not", text_review)
        text_review = re.sub(r"can\'t", "can not", text_review)

        # general
        text_review = re.sub(r"n\'t", " not", text_review)
        text_review = re.sub(r"\'re", " are", text_review)
        text_review = re.sub(r"\'s", " is", text_review)
        text_review = re.sub(r"\'d", " would", text_review)
        text_review = re.sub(r"\'ll", " will", text_review)
        text_review = re.sub(r"\'t", " not", text_review)
        text_review = re.sub(r"\'ve", " have", text_review)
        text_review = re.sub(r"\'m", " am", text_review)

        # remove special characters leaving only word and apostrophe
        text_review = re.sub("[^A-Za-z]+", ' ', text_review)

        text_token = text_review.split(' ')
        tokens_without_sw = [word for word in text_token if not word in stopwords]
        
        tempCorpus.append(' '.join(tokens_without_sw))

    return tempCorpus

class Tfidf():
    def __init__(self, corpus=1, nGram=1):
        self.wordsList = []
        self.wordsValues = []
        self.corpus = corpus
        self.nGram = nGram

    def __str__(self):
        return "<Test a:%s b:%s>" % (self.corpus, self.age)

    def vectorize():
        return



(tempCorpus, tempActualVal) = getReviews(directoryPos, 0, 1)
corpus += tempCorpus
review_actual_val += tempActualVal 

(tempCorpus, tempActualVal) = getReviews(directoryNeg, 0, 1)
corpus += tempCorpus
review_actual_val += tempActualVal 

corpus = filterData(corpus, stopwords)

tfidf_val = Tfidf([1],1)

print(tfidf_val)

