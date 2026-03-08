import faiss
import numpy as np


class FAISSStore:

    def __init__(self, dimension):

        self.index = faiss.IndexFlatIP(dimension)

        self.documents = []

    def add_documents(self, embeddings, docs):

        embeddings = np.array(embeddings).astype("float32")

        self.index.add(embeddings)

        self.documents.extend(docs)

    def search(self, query_embedding, k=5):

        query_embedding = np.array([query_embedding]).astype("float32")

        scores, indices = self.index.search(query_embedding, k)

        results = []

        for idx, score in zip(indices[0], scores[0]):

            results.append({
                "text": self.documents[idx]["text"],
                "category": self.documents[idx]["category"],
                "score": float(score)
            })

        return results