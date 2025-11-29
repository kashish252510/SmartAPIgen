from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from app.extractor import extract_basic_info, extract_basic_list
from app.extractor_full import extract_full_page
from app.fetcher import fetch_page

app = FastAPI()

# CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"status": "running", "message": "API Generator working!"}


# -----------------------------------------------------------
# BASIC INFO ENDPOINT
# -----------------------------------------------------------
@app.get("/api/v1/info")
def get_info(url: str = Query(...)):
    try:
        return extract_basic_info(url)
    except Exception as e:
        return {"error": str(e)}


# -----------------------------------------------------------
# LIST ENDPOINT (fetch HTML → extract list)
# -----------------------------------------------------------
@app.get("/api/v1/list")
async def get_list(url: str = Query(...)):
    try:
        html = await fetch_page(url)
        return extract_basic_list(html)
    except Exception as e:
        return {"error": str(e)}


# -----------------------------------------------------------
# FULL PAGE EXTRACTOR ENDPOINT
# -----------------------------------------------------------
@app.get("/api/v1/full")
def get_full(url: str = Query(...)):
    try:
        return extract_full_page(url)
    except Exception as e:
        return {"error": str(e)}
