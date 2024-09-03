# from openai import OpenAI
import openai
import os

# client = OpenAI()

openai.api_key=os.getenv("OPENAI_API_KEY")

def send_message(message, list_messages = []):
    list_messages.append({"role": "user", "content": message})
    
    response = openai.chat.completions.create(
        model="gpt-4o-mini",
        # messages=[{"role": "user", "content": message}],
        messages=list_messages,
        stream=True,
    )

    # response = openai.ChatCompletion.create(
    #     model="gpt-3.5.turbo",
    #     messages=[{"role": "user", "content": message}],
    # )

    # return response["choices"][0]["message"]["content"].strip()
    return response["choices"][0]["message"]

list_messages = []

while True:
    text = input("Escreva aqui a sua mensagem:")

    if text == "sair":
        break
    else :
        response = send_message(text, list_messages)
        list_messages.append(response)
        print(send_message("Chatbot: ", response["content"].strip()))

# print(send_message("Em que ano Einstein publicou a teoria da relatividade?"))

