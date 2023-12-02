from fastapi import FastAPI, UploadFile, File
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
import os

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

messageList = []

# Assuming "Fred.html" is in the same directory as this script
fred_html_path = os.path.join(os.path.dirname(__file__), "Fred.html")

@app_api.post('/api/send-html')
async def send_html_api(Fred: UploadFile = File(...)):
    html_content = await Fred.read()
    print(f"Received HTML content from file: {html_content}")
    messageList.append(html_content.decode("utf-8"))

    # Read HTML content from "Fred.html"
    with open(fred_html_path, "r", encoding="utf-8") as file:
        additional_html_content = file.read()

    # Combine the received HTML content and the additional HTML content
    final_html_content = html_content.decode("utf-8") + additional_html_content

    return HTMLResponse(content=final_html_content, status_code=200)
