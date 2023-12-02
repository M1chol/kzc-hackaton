import openai
from keys import OPENAI_API_KEY

class chatapigpt():
    def __init__(self) -> None:
        self.client = openai.OpenAI(api_key=OPENAI_API_KEY)

        # #TODO Temp switch
        # file_path = './test/programTestAi.txt'

        # with open(file_path, 'r') as file:
        #     self.fileContent = file.read()
        
    def contentMachine(self, title, code) -> str:
        completion = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Your job is to write documentation for this file including code snippets. Say OK if you understood."},
                {"role": "assistant", "content": "OK"},
                {"role": "user", "content": "Title of file is: " + title + "\n\nCode is:" + code}
            ]
        )
        return completion.choices[0].message.content

if __name__ == "__main__":
    test = chatapigpt()
    # print(chatapigpt.contentMachine(test, "main.py"))