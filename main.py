import os
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
import re

directoryPos = "./aclImdb/train/pos"

tokenized_pos = []
tokenized_neg = []

def remove_stop_words(tokenized_text):
    stop_words = set(stopwords.words("english"))
    tokenized_set = set(tokenized_text)

    # print(set_difference)
    return tokenized_set - stop_words


# Traverse pos train folder text files
posReviewList = os.listdir(directoryPos)
for x in range(10):
    if posReviewList[x].endswith(".txt"):
        
        # Open the text file
        filePath = directoryPos + "/" + posReviewList[x]
        file = open(filePath, "r", encoding="utf8")

        # tokenize data
        text_review = file.read()
        text_review = text_review.lower()

        # remove special characters leaving only word and apostrophe
        text_review = re.sub("[^A-Za-z']+",' ',text_review)
        text_data = text_review.split(' ')

        #text_data = remove_stop_words(text_data)
        tokenized_pos += text_data

print(len(tokenized_pos))
tokenized_pos = list(remove_stop_words(tokenized_pos))


# for filename in os.listdir(directoryPos):
#     if filename.endswith(".txt"):
#         # Open the text file
#         filePath = directoryPos + "/" + filename
#         file = open(filePath, "r", encoding="utf8")

#         # tokenize data
#         text_data = file.read().lower().split(' ')

#         #text_data = remove_stop_words(text_data)
#         tokenized_pos += text_data

#         continue
#     else:
#         continue

print(len(tokenized_pos))