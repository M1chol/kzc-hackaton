import markdown

#output = markdown.markdown('#hi')
#print(output)

with open('Fred.md', 'r') as file: #'r' = read, 'w' = write
    tempMD= file.read()

tempHTML = markdown.markdown(tempMD)

with open('Fred.html', 'w') as file: #print(tempHTML) podobno gorsze
    file.write(tempHTML)
print (tempHTML)
