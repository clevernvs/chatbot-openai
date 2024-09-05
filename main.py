from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()

response = client.chat.completions.create(
    # model="gpt-3.5-turbo",
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": "PT-BR: Ola Mundo! | ENG: Hello World!"}]
)


print(response.choices[0].message.content)
