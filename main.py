import os
from fastapi import FastAPI, Request
from google import genai

app = FastAPI()

client = genai.Client()

@app.post("/")
async def main(request: Request):
    body = await request.json()
    user_text = body["request"]["original_utterance"]

    response = client.models.generate_content(
        model="gemini-3.5-flash-lite",
        contents=user_text
    )
    answer = response.text

    return {
        "version": body["version"],
        "session": body["session"],
        "response": {
            "end_session": False,
            "text": answer
        }
    }
