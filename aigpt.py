import openai
import os
from keys import OPENAI_API_KEY

client = openai.OpenAI(api_key=OPENAI_API_KEY)

completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are assistant that likes to joke to much."},
        {"role": "user", "content": "How many ducks can fit in larges lake on earth?"}
    ]
)



print(completion)