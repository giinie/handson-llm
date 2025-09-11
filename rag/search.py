import json
import numpy as np

import faiss
from rank_bm25 import BM25Okapi
from sentence_transformers import SentenceTransformer


class HybridIndex:
    def __init__(self, model_name="all-MiniLM-L6-v2"):
        self.model = SentenceTransformer(model_name)
        self.records = []
        self.index = None
        self.bm25 = None

    def load(self, corpus_path="corpus.jsonl"):
        with open(corpus_path, "r", encoding="utf-8") as f:
            self.records = [json.loads(l) for l in f]
        embs = self.model.encode([r["text"] for r in self.records], normalize_embeddings=True)
        self.index = faiss.IndexFlatIP(embs.shape[1])
        self.index.add(embs)
        self.bm25 = BM25Okapi([r["text"].split() for r in self.records])

    def search(self, query, k=8, alpha=0.6):
        qv = self.model.encode([query], normalize_embeddings=True)
        D, I = self.index.search(qv, k * 5)
        vec = {int(i): float(s) for i, s in zip(I[0], D[0])}
        bm = self.bm25.get_scores(query.split())
        bmin, bmax = float(np.min(bm)), float(np.max(bm))
        scored = []
        for i in range(len(self.records)):
            v = vec.get(i, 0.0)
            b = (bm[i] - bmin) / (bmax - bmin + 1e-6)
            scored.append((0.0 if np.isnan(b) else alpha * v + (1 - alpha) * b, i))
        scored.sort(reverse=True)
        return [self.records[i] | {"id": i} for _, i in scored[:k]]


if __name__ == "__main__":
    idx = HybridIndex()
    idx.load()
    print(idx.search("캐시 무효화 전략", k=5))
