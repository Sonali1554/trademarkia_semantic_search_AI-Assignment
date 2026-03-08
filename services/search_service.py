import pickle
import faiss
import numpy as np

from embeddings.embedder import Embedder
from cache.semantic_cache import SemanticCache


INDEX_PATH = "data/processed/faiss.index"
DOC_STORE = "data/processed/doc_store.pkl"
CLUSTER_PATH = "data/processed/clusters.pkl"


class SearchService:

    def __init__(self):

        print("Loading embedding model...")
        self.embedder = Embedder()

        print("Loading FAISS index...")
        self.index = faiss.read_index(INDEX_PATH)

        print("Loading document store...")
        with open(DOC_STORE, "rb") as f:
            self.documents = pickle.load(f)

        print("Loading clustering data...")
        with open(CLUSTER_PATH, "rb") as f:
            cluster_data = pickle.load(f)

        self.cluster_centers = cluster_data["centers"]

        print("Initializing semantic cache...")
        self.cache = SemanticCache()

    def get_dominant_cluster(self, embedding):

        similarities = np.dot(self.cluster_centers, embedding)

        return int(np.argmax(similarities))

    def search(self, query):

        query_embedding = self.embedder.encode([query])[0]

        cluster_id = self.get_dominant_cluster(query_embedding)

        hit, item, sim = self.cache.lookup(query_embedding, cluster_id)

        if hit:

            return {
                "query": query,
                "cache_hit": True,
                "matched_query": item["query"],
                "similarity_score": float(sim),
                "result": item["result"],
                "dominant_cluster": cluster_id
            }

        query_vec = np.array([query_embedding]).astype("float32")

        scores, indices = self.index.search(query_vec, 5)

        results = []

        for idx, score in zip(indices[0], scores[0]):

            results.append({
                "text": self.documents[idx]["text"],
                "category": self.documents[idx]["category"],
                "score": float(score)
            })

        self.cache.add(query, query_embedding, results, cluster_id)

        return {
            "query": query,
            "cache_hit": False,
            "matched_query": None,
            "similarity_score": None,
            "result": results,
            "dominant_cluster": cluster_id
        }