import sys
import os
import asyncio

# -----------------------------------------------------------
# FIX WINDOWS PLAYWRIGHT SUBPROCESS (must be first!)
# -----------------------------------------------------------
if sys.platform == "win32":
    asyncio.set_event_loop_policy(asyncio.WindowsProactorEventLoopPolicy())


# -----------------------------------------------------------
# Now import everything else
# -----------------------------------------------------------
from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from app.extractor import extract_basic_info, extract_basic_list
from app.extractor_full import extract_full_page
from app.fetcher import fetch_page

# Routers (import AFTER fixing event loop)
from app.screenshot import router as screenshot_router
from app.pdf_export import router as pdf_router


# -----------------------------------------------------------
# CREATE APP
# -----------------------------------------------------------
app = FastAPI()


# -----------------------------------------------------------
# STATIC FILE SERVING
# -----------------------------------------------------------
SAVE_DIR = "static/saved_files"
os.makedirs(SAVE_DIR, exist_ok=True)

app.mount("/files", StaticFiles(directory=SAVE_DIR), name="files")


# -----------------------------------------------------------
# REGISTER ROUTERS (must be after app creation)
# -----------------------------------------------------------
app.include_router(screenshot_router, prefix="/api/v1")
app.include_router(pdf_router, prefix="/api/v1")


# -----------------------------------------------------------
# CORS SETTINGS
# -----------------------------------------------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# -----------------------------------------------------------
# ENDPOINTS
# -----------------------------------------------------------
@app.get("/")
def home():
    return {"status": "running", "message": "API Generator working!"}


@app.get("/api/v1/info")
def get_info(url: str = Query(...)):
    return extract_basic_info(url)


@app.get("/api/v1/list")
async def get_list(url: str = Query(...)):
    html = await fetch_page(url)
    return extract_basic_list(html)


@app.get("/api/v1/full")
def get_full(url: str = Query(...)):
    return extract_full_page(url)

