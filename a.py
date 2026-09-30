import os
from openai import OpenAI
from google import genai

TOKEN_HARBOR_API_KEY = "thk_live_ZDDtQNuyYlTEyvQLlNzqlHr6Gq5cAYjEonQS8ZWybRyQFOYkIH7sfER9s5HnfMDB"
OPENROUTER_API_KEY = "sk-or-v1-xxxxxxxxx"
GEMINI_API_KEY = "AIzaSyxxxxxxxxx"
OPENAI_API_KEY = "sk-xxxxxxxxx"

PROMPT = """
Chỉ viết CODE PYTHON để giải bài sau.
Không giải thích.
Không markdown.
Không ```.
Tối ưu thời gian và bộ nhớ.
Không cần đọc từ file INP OUT như đề bài, chỉ cần nhập từ bàn phím

"""

def token_harbor(de_bai):
    client = OpenAI(
        api_key=TOKEN_HARBOR_API_KEY,
        base_url="https://tokenharbor.ai/v1"
    )

    response = client.chat.completions.create(
        model="qwen3.8-flash:free",
        messages=[
            {"role": "system", "content": PROMPT},
            {"role": "user", "content": de_bai}
        ]
    )

    return response.choices[0].message.content


def openrouter(de_bai):
    client = OpenAI(
        api_key=OPENROUTER_API_KEY,
        base_url="https://openrouter.ai/api/v1"
    )

    response = client.chat.completions.create(
        model="openai/gpt-5",
        messages=[
            {"role": "system", "content": PROMPT},
            {"role": "user", "content": de_bai}
        ]
    )

    return response.choices[0].message.content


def gemini(de_bai):
    client = genai.Client(
        api_key=GEMINI_API_KEY
    )

    response = client.models.generate_content(
        model="gemini-3.8-flash",
        contents=PROMPT + "\n\nĐỀ BÀI:\n" + de_bai
    )

    return response.text


def chatgpt(de_bai):
    client = OpenAI(
        api_key=OPENAI_API_KEY
    )

    response = client.responses.create(
        model="gpt-5",
        instructions=PROMPT,
        input=de_bai
    )

    return response.output_text


def main():
    print("TH")
    print("OP")
    print("G")
    print("C")

    lua_chon = input("Chọn AI: ")

    if lua_chon not in ["1", "2", "3", "4"]:
        print("Lựa chọn không hợp lệ.")
        return

    print("\nNhập")
    print("END:\n")

    de_bai = []

    while True:
        dong = input()

        if dong == "END":
            break

        de_bai.append(dong)

    de_bai = "\n".join(de_bai)

    if not de_bai:
        print("Chưa nhập đề.")
        return

    print("\nĐang giải...\n")

    try:
        if lua_chon == "1":
            ket_qua = token_harbor(de_bai)
        elif lua_chon == "2":
            ket_qua = openrouter(de_bai)
        elif lua_chon == "3":
            ket_qua = gemini(de_bai)
        else:
            ket_qua = chatgpt(de_bai)

        print("=" * 60)
        print(ket_qua)
        print("=" * 60)

    except Exception as e:
        print("Lỗi:", e)


if __name__ == "__main__":
    main()
