# DealLens

> Due diligence lives in 12 tabs. We put it in one.

DealLens is an AI-powered pitch deck analyzer for VCs. Upload any pitch deck and get a structured deal snapshot in 30 seconds — then generate a full partner-ready investment memo in one click.

---

## Features

**Deal Snapshot** — Drop a PDF or PPTX pitch deck. Claude reads it and returns:
- Company overview & one-liner
- Founder backgrounds
- Market sizing (TAM / SAM / SOM)
- Traction & key metrics
- Competitive landscape
- Red flags
- Key questions to ask in the meeting
- Preliminary verdict (Pass / Explore / Fast-track)

**Investment Memo** — One click from the snapshot. Claude writes a full structured memo with 8 sections, ready to share with your partnership.

---

## Stack

| Layer | Tech |
|---|---|
| Frontend | Vanilla HTML/CSS/JS |
| Backend | FastAPI + Uvicorn |
| AI | Claude (claude-sonnet-4-6) via Anthropic SDK |
| PDF parsing | PyMuPDF (fitz) |
| PPTX parsing | python-pptx |

---

## Quickstart

**1. Clone the repo**
```bash
git clone https://github.com/Taytottyy/deallens.git
cd deallens
```

**2. Install dependencies**
```bash
pip install fastapi uvicorn anthropic pymupdf python-pptx python-multipart
```

**3. Set your Anthropic API key**

Get one at [console.anthropic.com](https://console.anthropic.com)
```bash
export ANTHROPIC_API_KEY=sk-ant-...
```

**4. Start the server**
```bash
uvicorn backend.main:app --host 0.0.0.0 --port 8000 --reload
```

**5. Open the app**

| Page | URL |
|---|---|
| Deal Snapshot | http://localhost:8000/app.html |
| Investment Memo | http://localhost:8000/memo.html |
| Landing Page | http://localhost:8000/landing.html |

---

## Project Structure

```
deallens/
├── landing.html          # Marketing landing page
├── app.html              # Deal snapshot app
├── memo.html             # Investment memo generator
├── docs.html             # Documentation
├── backend/
│   ├── main.py           # FastAPI server + API endpoints
│   └── requirements.txt  # Python dependencies
├── prompts/
│   ├── deal_snapshot.md  # System prompt for deal analysis
│   └── investment_memo.md # System prompt for memo generation
└── assets/               # Static assets
```

---

## API Endpoints

`POST /analyze` — Upload a pitch deck, get back a deal snapshot JSON

`POST /generate-memo` — Send a snapshot JSON, get back an investment memo as HTML

---

Built at a hackathon in 2 hours. Powered by Claude.
