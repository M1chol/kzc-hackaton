import openai
from keys import OPENAI_API_KEY

# OPENAI_API_KEY = os.getenv('GPT_API_KEY')


client = openai.OpenAI(api_key=OPENAI_API_KEY)

file_path = './test/programTestAi.txt'

with open(file_path, 'r') as file:
    fileContent = file.read()

completion1 = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "Your job is to give part of code and make short documentation of code given. Say OK if you understood."},
        {"role": "assistant", "content": "OK"},
        {"role": "user", "content": fileContent}
    ]
)

completion2 = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "Your job is to link parts of code in snippets with relevent parts of documentation. Say OK if you understood."},
        {"role": "assistant", "content": "OK"},
        {"role": "user", "content": '\n\nCode:\n' + fileContent + '\n\nDocumentation:\n' + completion1.choices[0].message.content}
    ]
)

completion3 = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "Your job is to convert given documentation into one raw markdown file. Say OK if you understood."},
        {"role": "assistant", "content": "OK"},
        {"role": "user", "content": completion2.choices[0].message.content}
    ]
)

content = completion3.choices[0].message.content
print(type(content))
print(content)