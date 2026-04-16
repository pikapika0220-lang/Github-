from openai import OpenAI

client = OpenAI(api_key="ここにAPIキー貼る")

response = client.responses.create(
    model="gpt-5-mini",input="大阪の天気を一言で説明して")

print(response.output_text)