import markdown
from aigpt import chatapigpt

test = chatapigpt()

stringi = test.contentMachine()
#output = markdown.markdown('#hi')
#print(output)

tempHTML = markdown.markdown(stringi)
