import math

def cosine_similarity(a: list[float], b: list[float]) -> float:
    dot = sum(x * y for x, y in zip(a, b))
    norm_a = math.sqrt(sum(x * x for x in a))
    norm_b = math.sqrt(sum(y * y for y in b))
    if norm_a == 0 or norm_b == 0:
        return 0.0
    return dot / (norm_a * norm_b)

def top_k_similar(query_embedding: list[float], candidates: list[dict], k: int) -> list[dict]:
    """candidates: [{"text": str, "embedding": list[float], ...}] -> top-k by similarity, most similar first"""
    scored = [
        {**c, "similarity": cosine_similarity(query_embedding, c["embedding"])}
        for c in candidates
    ]
    scored.sort(key=lambda c: c["similarity"], reverse=True)
    return scored[:k]
