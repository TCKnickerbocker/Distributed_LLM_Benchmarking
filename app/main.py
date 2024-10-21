from fastapi import FastAPI
from pydantic import BaseModel
from model import generate_text

app = FastAPI()

class TextGenerationRequest(BaseModel):
    prompt: str

@app.post("/generate/")
def generate_text_endpoint(request: TextGenerationRequest):
    generated_text = generate_text(request.prompt)
    return {"generated_text": generated_text}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
