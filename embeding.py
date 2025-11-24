# src/embed.py
from sentence_transformers import SentenceTransformer
import numpy as np
import faiss
import pandas as pd
import os
import pickle

MODEL_NAME = "all-MiniLM-L6-v2"

def build_embeddings(docs, model_name=MODEL_NAME):
    model = SentenceTransformer(model_name)
    embeddings = model.encode(docs, show_progress_bar=True, convert_to_numpy=True)
    return embeddings

def build_faiss_index(embeddings, index_path="data/faiss.idx", meta=None):
    d = embeddings.shape[1]
    index = faiss.IndexFlatL2(d)
    index.add(embeddings)
    faiss.write_index(index, index_path)
    if meta:
        with open(index_path + ".meta.pkl", "wb") as f:
            pickle.dump(meta, f)
    return index_path

def load_index(index_path="data/faiss.idx"):
    index = faiss.read_index(index_path)
    with open(index_path + ".meta.pkl", "rb") as f:
        meta = pickle.load(f)
    return index, meta
