import numpy as np
import gensim
import pandas as pd


# corona_data = [text for text in data if text.count(' ') >= 2]


def pre_process():
    file = open('aclImdb/train/pos/0_9.txt', 'r')
    review_text = file.readline()
    file.close()
    return gensim.utils.simple_preprocess(review_text)


def cbow_model(window, data):
    target = int(window / 2)
    train_set_f = open('train_set.txt', 'w')

    for i in range(len(data) - (int(window / 2) + 1)):
        begin = target - 1
        end = target + 1
        train_set_f.write(data[begin] + ',' + data[end] + ',' + data[target])
        train_set_f.write(',\n')
        # increment the target word
        target = target + 1




text = pre_process()
vocab_length = len(text)
embed_dim = 10

embeddings = np.random.random_sample((vocab_length, embed_dim))

cbow_model(2, text)

train()
