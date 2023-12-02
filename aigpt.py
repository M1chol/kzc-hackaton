import openai
import os
from keys import OPENAI_API_KEY

client = openai.OpenAI(api_key=OPENAI_API_KEY)

completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "Your job is to make documentation from code given by he user. Say OK if you understood."},
        {"role": "assistant", "content": "OK"},
        {"role": "user", "content": ""}
    ]
)

print(completion)