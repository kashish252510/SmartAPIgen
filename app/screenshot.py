from fastapi import APIRouter, Query
from playwright.async_api import async_playwright
import uuid
import os

router = APIRouter()

SAVE_DIR = "static/saved_files"
os.makedirs(SAVE_DIR, exist_ok=True)

@router.get("/screenshot")
async def capture_screenshot(url: str = Query(...)):
    try:
        filename = f"screenshot_{uuid.uuid4().hex}.png"
        filepath = os.path.join(SAVE_DIR, filename)

        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=True)
            page = await browser.new_page()

            await page.goto(url, timeout=60000)
            await page.screenshot(path=filepath, full_page=True)
            await browser.close()

        return {
            "status": "success",
            "image_url": f"http://127.0.0.1:8000/files/{filename}"
        }

    except Exception as e:
        return {"status": "error", "message": str(e)}
