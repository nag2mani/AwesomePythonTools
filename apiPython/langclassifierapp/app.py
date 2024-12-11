from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from langdetect import detect

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins
    allow_methods=["GET", "POST"],  # Allow GET method
    allow_headers=["*"],  # Allow all headers
)

@app.get("/detect-language")
def detect_language(text: str):
    try:
        language = detect(text)
        return {"input": text, "output": language}
    except Exception as e:
        return {"error": "LanguageNotREcogniseError"}
    