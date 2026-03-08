from sentence_transformers import SentenceTransformer
import numpy as np
#Normalization allows cosine similarity to be computed using dot product,which is optimized in FAISS.

class Embedder:

    def __init__(self, model_name="all-MiniLM-L6-v2"):

        self.model = SentenceTransformer(model_name)

    def encode(self, texts):

        embeddings = self.model.encode(
            texts,
            show_progress_bar=True,
            normalize_embeddings=True
        )

        return np.array(embeddings)