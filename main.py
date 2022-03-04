import os
import nltk
from nltk.corpus import stopwords

directoryPos = "./aclImdb/train/pos"

tokenized_pos = []
tokenized_neg = []


def remove_stop_words(tokenized_text):
    stop_words = list(stopwords.words("english"))
    for w in tokenized_text:
        if w in stop_words:
            print(w + " removed ")
            tokenized_text.remove(w)
            continue

    return tokenized_text


# Traverse pos train folder text files
for filename in os.listdir(directoryPos):
    if filename.endswith(".txt"):
        # Open the text file
        filePath = directoryPos + "/" + filename
        file = open(filePath, "r")

        # tokenize data
        text_data = file.read().lower().split(' ')
        tokenized_pos.append(text_data)

        continue
    else:
        continue

print(len(tokenized_pos))

tokenized_pos = remove_stop_words(tokenized_pos)

print(len(tokenized_pos))
