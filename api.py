from fastapi import FastAPI, Form
from fastapi.middleware.cors import CORSMiddleware
from aigpt import chatapigpt
from markdownFunction import MarkToHtml

app_api = FastAPI()

# CORS (Cross-Origin Resource Sharing) configuration
origins = ["http://127.0.0.1:5000"]  # Update this with the actual origin of your Flask app

app_api.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app_api.post('/api/send-text')
def send_text_api(text: str = Form(...), title: str = Form()):
    GPT_Instance = chatapigpt()
    raw = GPT_Instance.contentMachine(title, text)
    # wywołanie funkcji basi
    html = MarkToHtml(raw)

    return {"raw": raw, "html":html}

@app_api.get('/api/get-text')
def get_text():
    return