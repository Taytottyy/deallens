# DealLens Backend
# FastAPI server for pitch deck analysis

from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="DealLens API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"status": "ok", "service": "DealLens API"}

@app.post("/analyze")
async def analyze_deck(file: UploadFile = File(...)):
    # 1. Extract text from PDF/PPTX
    # 2. Send to Claude with deal_snapshot prompt
    # 3. Return structured snapshot
    return {"message": "not implemented yet"}

@app.post("/generate-memo")
async def generate_memo(snapshot: dict):
    # 1. Take deal snapshot as input
    # 2. Send to Claude with investment_memo prompt
    # 3. Return full memo + export as PDF
    return {"message": "not implemented yet"}
