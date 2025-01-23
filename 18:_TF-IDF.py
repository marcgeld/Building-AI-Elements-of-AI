import math

import numpy as np

text = '''Humpty Dumpty sat on a wall
Humpty Dumpty had a great fall
all the king's horses and all the king's men
couldn't put Humpty together again'''


def main(text):
    docs = [line.split() for line in text.splitlines()]

    N = len(docs)
    vocabulary = list(set(text.split()))

    df = {}
    tf = {}
    for word in vocabulary:
        tf[word] = [doc.count(word) / len(doc) for doc in docs]
        df[word] = sum([word in doc for doc in docs]) / N

    rows = []
    for doc_index, doc in enumerate(docs):
        tfidf = []
        for word in vocabulary:
            tf_idf_val = tf[word][doc_index] * math.log(1 / df[word], 10)
            tfidf.append(tf_idf_val)
        rows.append(tfidf)
    dist = [[sum(abs(np.asarray(r0) - np.asarray(r1))) for r0 in rows] for r1 in rows]
    dist = np.asarray(dist).astype('float')
    dist[dist == 0] = np.nan
    dist_ur = (np.unravel_index(np.nanargmin(dist), dist.shape))
    print(dist_ur)

main(text)