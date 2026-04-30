from openai import OpenAI
import numpy as np

client = OpenAI(api_key='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')

# 参照するドキュメント（自社データのイメージ）
documents = [
    "豊増社の営業時間は9時から18時です",
    "豊増社の返品期限は購入から30日以内です",
    "豊増社のサポートメールはtoyomasu@example.comです",
    "豊増社の送料は全国一律500円です",
]

# ドキュメントをEmbeddingsで数値化する(data,usage,数値含む)
response = client.embeddings.create(
    model="text-embedding-3-small",
    input=documents
)

doc_embeddings = [item.embedding for item in response.data] #dataでデータのみ取り出す,embeddingで数値を取り出す
print("ドキュメントの数値化完了！")

# ユーザーの質問を数値化する
question = input("質問を入力してください: ")
question_response = client.embeddings.create(
    model="text-embedding-3-small",
    input=[question]
)
question_embedding = question_response.data[0].embedding

# 各ドキュメントとの類似度を計算する
def cosine_similarity(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

similarities = [cosine_similarity(question_embedding, doc_emb) for doc_emb in doc_embeddings]

# 一番類似度が高いドキュメントを取得する
most_similar_index = np.argmax(similarities)#最大となるリスト番号を返す
most_similar_doc = documents[most_similar_index]

# 見つかったドキュメントをLLMに渡して回答を生成する
response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": f"以下の情報を元に答えてください。\n{most_similar_doc}"},
        {"role": "user", "content": question}
    ]
)

print(f"回答: {response.choices[0].message.content}")