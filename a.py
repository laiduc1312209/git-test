from openai import OpenAI

TOKEN_HARBOR_API_KEY = "thk_live_ZDDtQNuyYlTEyvQLlNzqlHr6Gq5cAYjEonQS8ZWybRyQFOYkIH7sfER9s5HnfMDB"

PROMPT = """
Chỉ trả về CODE PYTHON.
Không giải thích.
Không markdown.
Không ```.
Tối ưu thời gian và bộ nhớ.
Chỉ dùng input() và print().
"""

client = OpenAI(
    api_key=TOKEN_HARBOR_API_KEY,
    base_url="https://tokenharbor.ai/v1"
)

de_bai = input(": ")

print("\nĐang\n")

try:
    stream = client.chat.completions.create(
        model="qwen3.8-flash:free",
        messages=[
            {"role": "system", "content": PROMPT},
            {"role": "user", "content": de_bai}
        ],
        stream=True
    )

    for chunk in stream:
        if chunk.choices and chunk.choices[0].delta.content:
            print(chunk.choices[0].delta.content, end="", flush=True)

    print()

except Exception as e:
    print("Lỗi:", e)
