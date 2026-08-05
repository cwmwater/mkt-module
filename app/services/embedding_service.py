from app.services.gpt_service import client

EMBEDDING_MODEL = "text-embedding-3-small"

def get_embedding(text: str) -> list[float]:
    response = client.embeddings.create(
        model=EMBEDDING_MODEL,
        input=text,
    )
    return response.data[0].embedding
