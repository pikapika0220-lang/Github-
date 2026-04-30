from openai import OpenAI
import numpy as np
client = OpenAI(api_key='APIkey')

response = client.embeddings.create(
    model="text-embedding-3-small",
    input=["犬が公園で走っている", "中日ドラゴンズが5連敗した"]
)

embedding1 = response.data[0].embedding
embedding2 = response.data[1].embedding

# コサイン類似度を計算する
def cosine_similarity(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

similarity = cosine_similarity(embedding1, embedding2)
print(f"類似度: {similarity}")