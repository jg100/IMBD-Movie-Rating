import os
import nltk
from nltk import RegexpTokenizer
from nltk.corpus import stopwords
from BoW import *
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd
import re


def main():
    directory_pos = "./aclImdb/train/pos"

    tokenized_pos = []
    pos_documents = []
    tokenized_neg = []

    # Traverse pos train folder text files
    for filename in os.listdir(directory_pos):
        if filename.endswith(".txt"):
            # Open the text file
            file_path = directory_pos + "/" + filename
            file = open(file_path, "r", encoding="utf8")

            file_data = file.read().lower()
            # tokenize data

            tokenizer = RegexpTokenizer(r'\w+')
            
            # remove special characters leaving only word and apostrophe
            file_data = re.sub("[^A-Za-z']+",' ',file_data)
            text_data = tokenizer.tokenize(file_data)
            stop_words = stopwords.words("english")

            # for w in text_data:
            #     if w in stop_words or len(w) <= 1 or w.startswith(r'[0-9]'):
            #         print("Removed: " + w)
            #         text_data.remove(w)

            # text_data = remove_stop_words(text_data)
            # pos_documents.append(str(text_data))
            pos_documents.append(' '.join(str(x) for x in text_data))
            tokenized_pos += text_data

            continue
        else:
            continue
    print(pos_documents)
    print("Length of pos_documents: " + str(len(pos_documents)))
    bag_of_words(pos_documents)






def remove_stop_words(pos_documents):
    stop_words = stopwords.words("english")
    for d in pos_documents:
        for w in d:
            if w in stop_words or len(w) <= 1:
                # print("REMOVED: " + w)
                d.remove(w)


def bag_of_words(list_of_docs):
    vectorizer = CountVectorizer()
    X = vectorizer.fit_transform(list_of_docs)
    print(vectorizer.get_feature_names_out())

    df_bow_sklearn = pd.DataFrame(X.toarray(), columns=vectorizer.get_feature_names())
    print(df_bow_sklearn)


if __name__ == "__main__":
    main()
