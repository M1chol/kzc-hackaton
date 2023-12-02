import openai
from keys import OPENAI_API_KEY

class chatapigpt():
    def __init__(self) -> None:
        self.client = openai.OpenAI(api_key=OPENAI_API_KEY)

        #TODO Temp switch
        file_path = './test/programTestAi.txt'

        with open(file_path, 'r') as file:
            self.fileContent = file.read()
        
    def contentMachine(self, fileContent, title) -> str:
        completion1 = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Your job is to give part of code and make short documentation of code given. Say OK if you understood."},
                {"role": "assistant", "content": "OK"},
                {"role": "user", "content": "Title of file is: " + title + "\n\nCode is:" + self.fileContent}
            ]
        )

        completion2 = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Your job is to link parts of code in snippets with relevent parts of documentation. Say OK if you understood."},
                {"role": "assistant", "content": "OK"},
                {"role": "user", "content": '\n\nCode:\n' + self.fileContent + '\n\nDocumentation:\n' + completion1.choices[0].message.content}
            ]
        )

        completion3 = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Your job is to convert given documentation into one raw markdown file. Say OK if you understood."},
                {"role": "assistant", "content": "OK"},
                {"role": "user", "content": completion2.choices[0].message.content}
            ]
        )

        content = completion3.choices[0].message.content
        return content
