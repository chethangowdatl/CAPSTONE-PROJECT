# src/retriever.py
from src.embed import build_embeddings, load_index
from sentence_transformers import SentenceTransformer
import numpy as np

MODEL_NAME = "all-MiniLM-L6-v2"

class Retriever:
    def __init__(self, index_path="data/faiss.idx"):
        self.index, self.meta = load_index(index_path)
        self.model = SentenceTransformer(MODEL_NAME)

    def retrieve(self, query, top_k=3):
        q_emb = self.model.encode([query], convert_to_numpy=True)
        D, I = self.index.search(q_emb, top_k)
        results = []
        for idx in I[0]:
            results.append(self.meta[idx])  # meta should include text & source
        return results
