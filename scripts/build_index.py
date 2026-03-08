import json
import pickle
import os

from embeddings.embedder import Embedder
from vector_store.faiss_store import FAISSStore


PROCESSED_DATA = "data/processed/documents.json"
INDEX_PATH = "data/processed/faiss.index"
DOC_STORE = "data/processed/doc_store.pkl"


def main():

    print("Loading processed documents...")

    with open(PROCESSED_DATA, "r") as f:
        docs = json.load(f)

    texts = [d["text"] for d in docs]

    print("Total documents:", len(texts))

    print("Loading embedding model...")

    embedder = Embedder()

    embeddings = embedder.encode(texts)

    dim = embeddings.shape[1]

    print("Embedding dimension:", dim)

    store = FAISSStore(dim)

    print("Adding embeddings to FAISS...")

    store.add_documents(embeddings, docs)

    print("Saving FAISS index...")

    import faiss
    faiss.write_index(store.index, INDEX_PATH)

    print("Saving document store...")

    with open(DOC_STORE, "wb") as f:
        pickle.dump(store.documents, f)

    print("Index built successfully!")


if __name__ == "__main__":
    main()