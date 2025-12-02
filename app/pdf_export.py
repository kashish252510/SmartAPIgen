from fastapi import APIRouter, Query
from playwright.async_api import async_playwright
import os, time

router = APIRouter()

SAVE_DIR = "static/saved_files"
os.makedirs(SAVE_DIR, exist_ok=True)


@router.get("/export-pdf")
async def export_pdf(url: str = Query(...)):
    filename = f"website_{int(time.time())}.pdf"
    filepath = os.path.join(SAVE_DIR, filename)

    try:
        async with async_playwright() as p:
            browser = await p.chromium.launch(
                headless=True,
                args=["--no-sandbox"]
            )
            page = await browser.new_page()
            await page.goto(url, timeout=80000)

            await page.pdf(path=filepath, format="A4")

            await browser.close()

        return {
            "status": "success",
            "file_url": f"http://127.0.0.1:8000/files/{filename}"
        }

    except Exception as e:
        return {"status": "error", "message": str(e)}
