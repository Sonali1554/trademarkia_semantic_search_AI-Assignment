import pickle
import numpy as np
import faiss

from clustering.fuzzy_cluster import FuzzyCluster

INDEX_PATH = "data/processed/faiss.index"
DOC_STORE = "data/processed/doc_store.pkl"
CLUSTER_OUTPUT = "data/processed/clusters.pkl"


def main():

    print("Loading FAISS index...")

    index = faiss.read_index(INDEX_PATH)

    embeddings = index.reconstruct_n(0, index.ntotal)

    print("Embeddings shape:", embeddings.shape)

    print("Running fuzzy clustering...")

    cluster_model = FuzzyCluster(n_clusters=15)

    memberships = cluster_model.fit(embeddings)

    print("Saving clustering results...")

    with open(CLUSTER_OUTPUT, "wb") as f:

        pickle.dump({
            "centers": cluster_model.centers,
            "membership": memberships
        }, f)

    print("Clustering completed.")


if __name__ == "__main__":
    main()