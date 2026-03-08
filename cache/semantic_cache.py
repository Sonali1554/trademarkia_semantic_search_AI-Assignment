import numpy as np
from sklearn.metrics.pairwise import cosine_similarity


class SemanticCache:

    def __init__(self, similarity_threshold=0.85):

        self.cache = []

        self.similarity_threshold = similarity_threshold

        self.hit_count = 0
        self.miss_count = 0

    def lookup(self, query_embedding, cluster_id):

        for item in self.cache:

            if item["cluster"] != cluster_id:
                continue

            sim = cosine_similarity(
                [query_embedding],
                [item["embedding"]]
            )[0][0]

            if sim >= self.similarity_threshold:

                self.hit_count += 1

                return True, item, sim

        self.miss_count += 1

        return False, None, None

    def add(self, query, embedding, result, cluster):

        self.cache.append(
            {
                "query": query,
                "embedding": embedding,
                "result": result,
                "cluster": cluster
            }
        )

    def stats(self):

        total = len(self.cache)

        total_queries = self.hit_count + self.miss_count

        hit_rate = self.hit_count / total_queries if total_queries > 0 else 0

        return {
            "total_entries": total,
            "hit_count": self.hit_count,
            "miss_count": self.miss_count,
            "hit_rate": hit_rate
        }

    def clear(self):

        self.cache = []
        self.hit_count = 0
        self.miss_count = 0