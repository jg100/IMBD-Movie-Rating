import numpy as np


# Activation function
def sigmoid(x):
    return 1 / (1 + np.exp(-x))


def predict(input_vector, weights, bias):
    layer_1 = np.dot(input_vector, wieghts) + bias
    layer_2 = sigmoid(layer_1)
    return layer_2


# Function used to measure error is the Mean Squared Error
def mse_loss(prediction, target):
    return np.square(prediction - target)


def one_hot_encode(id, vocab_size):
    res = [0] * vocab_size
    res[id] = 1
    return res


# train function using nueral network and back prop
def train():
    file = open('vocab_test.txt', 'r')
    vocab = file.readline().lower().split()

    train_file = open('train_set.txt', 'r')
    train_test = train_file.readline().split(',')

    # generate one hot encoding for each word in train set
    w_1_vec = np.zeros(len(vocab), dtype=int)
    w_2_vec = np.zeros(len(vocab), dtype=int)
    expected_vec = np.zeros(len(vocab), dtype=int)

    # one hot vector encodings
    w_1_vec[vocab.index(train_test[0])] = 1
    w_2_vec[vocab.index(train_test[1])] = 1

    weight_vec = np.random.random_sample((len(w_1_vec), 4))
    expected_vec[vocab.index(train_test[2])] = 1

    matrix = np.stack(weight_vec[vocab.index(train_test[0])], weight_vec[vocab.index(train_test[0])]))

    # weight vectors and hidden layer: dot products and sum
    dot_w1 = np.dot(w_1_vec, weight_vec)
    dot_w2 = np.dot(w_2_vec, weight_vec)

    print(dot_w1)
    print(dot_w2)


train()
