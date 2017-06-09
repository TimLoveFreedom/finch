from brown import get_indexed
from sklearn.manifold import TSNE
from sklearn.feature_extraction.text import TfidfTransformer
from utils import find_analogy
import numpy as np
import matplotlib.pyplot as plt


if __name__ == '__main__':
    indexed, word2idx = get_indexed(min_freq=5)
    vocab_size = len(word2idx)
    print("Data loaded | Vocab size:", vocab_size, '| Document size:', len(indexed))

    TD = np.zeros((vocab_size, len(indexed))) # term-document matrix
    j = 0
    for indices in indexed:
        for idx in indices:
            TD[idx, j] += 1
        j += 1
    print("Term-Document matrix built ...")

    model = TfidfTransformer()
    DT = TD.T
    DT = model.fit_transform(DT).toarray()
    TD = DT.T
    print("TF-IDF transform completed ...")

    find_analogy('london', TD, word2idx)
    find_analogy('king', TD, word2idx)

    """
    model = TSNE(n_components=2, verbose=2, learning_rate=200)
    X = model.fit_transform(TD)
    print("TSNE transform completed ...")
    """

    """
    idx2word = {idx : word for word, idx in word2idx.items()}
    plt.scatter(X[:,0], X[:,1])
    for i in range(vocab_size):
        try:
            plt.annotate(s=idx2word[i], xy=(X[i,0], X[i,1]))
        except:
            print("bad string:", idx2word[i])
    plt.show()
    """