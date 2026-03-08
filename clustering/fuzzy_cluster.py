import numpy as np
import skfuzzy as fuzz


class FuzzyCluster:

    def __init__(self, n_clusters=15):
        self.n_clusters = n_clusters
        self.centers = None
        self.membership = None

    def fit(self, embeddings):

        embeddings = embeddings.T

        cntr, u, _, _, _, _, _ = fuzz.cluster.cmeans(
            embeddings,
            c=self.n_clusters,
            m=2,
            error=0.005,
            maxiter=1000,
            init=None
        )

        self.centers = cntr
        self.membership = u

        return u

    def get_dominant_cluster(self, doc_index):

        memberships = self.membership[:, doc_index]

        return np.argmax(memberships)