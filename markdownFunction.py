import markdown

def MarkToHtml(tempMD: str) -> str:
    return markdown.markdown(tempMD)

