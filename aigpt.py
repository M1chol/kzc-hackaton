import openai
import os
from keys import OPENAI_API_KEY

client = openai.OpenAI(api_key=OPENAI_API_KEY)

file_path = './test/programTestAi.txt'

with open(file_path, 'r') as file:
    fileContent = file.read()

completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "Your job is to make documentation in markdown format from code given by he user. Say OK if you understood."},
        {"role": "assistant", "content": "OK"},
        {"role": "user", "content": fileContent}
    ]
)

# print(completion["choices"][0]["message"]["content"])
content = completion.choices[0].message.content
print(content)