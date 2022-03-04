import os
import nltk
from nltk.corpus import stopwords

directoryPos = "./aclImdb/train/pos"

tokenized_pos = []
tokenized_neg = []


def remove_stop_words(tokenized_text):
    stop_words = set(stopwords.words("english"))
    tokenized_set = set(tokenized_text)
    set_difference = tokenized_set - stop_words
    print(set_difference)
    return tokenized_set - stop_words


# Traverse pos train folder text files
for filename in os.listdir(directoryPos):
    if filename.endswith(".txt"):
        # Open the text file
        filePath = directoryPos + "/" + filename
        file = open(filePath, "r")

        # tokenize data
        text_data = file.read().lower().split(' ')

        #text_data = remove_stop_words(text_data)
        tokenized_pos += text_data

        continue
    else:
        continue

print(len(tokenized_pos))


