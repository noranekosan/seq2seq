# coding: utf-8
import sys
sys.path.append('..')
import os
import numpy as np


id_to_char = {}
word_to_id = {}


def _update_vocab(txt):
    word = list(txt)

    for i, word in enumerate(word):
        if word not in word_to_id:
            tmp_id = len(word_to_id)
            word_to_id[word] = tmp_id
            id_to_char[tmp_id] = word


def load_data(file_name='token.ta', seed=1984):
    file_path = os.path.dirname(os.path.abspath(__file__)) + '/' + file_name

    if not os.path.exists(file_path):
        print('No file: %s' % file_name)
        return None

    questions, answers = [], []

    for line in open(file_path, 'r', encoding='utf-8'):
        idx = line.find('_')
        questions.append(line[:idx])
        answers.append(line[idx:-1])

    # create vocab dict
    for i in range(len(questions)):
        q, a = questions[i], answers[i]
        _update_vocab(q)
        _update_vocab(a)

    # create numpy array
    x = np.zeros((len(questions), 64), dtype=np.int)
    t = np.zeros((len(answers), 64), dtype=np.int)
    try:
        for i, sentence in enumerate(questions):
            ids = [word_to_id[c] for c in sentence.split('_')]
            x[i] = np.append(ids, np.full(64-len(ids),word_to_id['_']))
        for i, sentence in enumerate(answers):
            ids = [word_to_id[c] for c in sentence.split('_')]
            t[i] = np.append(ids, np.full(64-len(ids),word_to_id['_']))
    except KeyError:
        pass

    # shuffle
    indices = np.arange(len(x))
    if seed is not None:
        np.random.seed(seed)
    np.random.shuffle(indices)
    x = x[indices]
    t = t[indices]

    # 10% for validation set
    split_at = len(x) - len(x) // 10
    (x_train, x_test) = x[:split_at], x[split_at:]
    (t_train, t_test) = t[:split_at], t[split_at:]

    return (x_train, t_train), (x_test, t_test)


def get_vocab():
    return word_to_id, id_to_char
