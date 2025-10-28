from fastapi import FastAPI, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
from io import BytesIO
from llm_chain import summarize_dataframe

app = FastAPI(title="AI-Assisted Hypothesis Explorer API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/summarize")
async def summarize(question: str = Form(...), file: UploadFile = File(...)):
    content = await file.read()
    df = pd.read_csv(BytesIO(content))
    summary = summarize_dataframe(df, question)
    return {"summary": summary}
