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
        completion1 = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Your job is to give part of code and make short documentation of code given. Say OK if you understood."},
                {"role": "assistant", "content": "OK"},
                {"role": "user", "content": "Title of file is: " + title + "\n\nCode is:" + code}
            ]
        )

        completion2 = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Your job is to add to parts of documentation corresponding code snippets."},
                # {"role": "assistant", "content": "OK"},
                {"role": "user", "content": "Code:\n" + code + "\n\nDocumentation:\n" + completion1.choices[0].message.content}
            ]
        )

        # completion3 = self.client.chat.completions.create(
        #     model="gpt-3.5-turbo",
        #     messages=[
        #         {"role": "system", "content": "Your job is to convert given documentation into one raw markdown file. Say OK if you understood."},
        #         {"role": "assistant", "content": "OK"},
        #         {"role": "user", "content": completion2.choices[0].message.content}
        #     ]
        # )

        return completion2.choices[0].message.content

if __name__ == "__main__":
    test = chatapigpt()
    # print(chatapigpt.contentMachine(test, "main.py"))