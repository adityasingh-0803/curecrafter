# PaperMinerAgent — Extract biomedical triples using OpenAI

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import openai
import os

app = FastAPI()

class Request(BaseModel):
    abstract: str
    api_key: str

@app.post("/extract-triples")
def extract_triples(data: Request):
    try:
        openai.api_key = data.api_key
        prompt = f"""
From the abstract below, extract triples of the form: (Gene, Drug, Disease)

Abstract:
{data.abstract}

Output format:
[("GENE1", "DRUG1", "DISEASE1"), ...]
"""
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}]
        )
        content = response["choices"][0]["message"]["content"]
        triples = eval(content.strip())
        return {"triples": triples}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
