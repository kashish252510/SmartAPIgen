document.getElementById("fetchBtn").addEventListener("click", async () => {
    const url = document.getElementById("urlInput").value.trim();
    const endpoint = document.getElementById("endpointSelect").value;
    const output = document.getElementById("output");

    if (!url.startsWith("http")) {
        output.textContent = "❌ Please enter a valid URL starting with https://";
        return;
    }

    output.textContent = "⏳ Fetching data...";

    try {
        const apiURL = `http://127.0.0.1:8000/api/v1/${endpoint}?url=${encodeURIComponent(url)}`;
        const response = await fetch(apiURL);

        if (!response.ok) throw new Error("Backend error");

        const data = await response.json();

        // --------------------------------------------
        // ✅ 1. SCREENSHOT HANDLING (Thum.io URL)
        // --------------------------------------------
        if (endpoint === "screenshot") {
            output.innerHTML = `
                <p>✅ Screenshot Captured</p>

                <img src="${data.image_url}" 
                     style="width:100%;max-width:650px;border:1px solid #555;border-radius:8px;margin-top:10px"/>

                <br><br>

                <button id="downloadBtn" 
                        style="padding:10px 15px;background:#0ea5e9;color:white;border:none;border-radius:6px;cursor:pointer;">
                    ⬇ Download Screenshot
                </button>
            `;

            // Download button logic
            document.getElementById("downloadBtn").addEventListener("click", () => {
                window.open(data.image_url, "_blank");
            });

            return;
        }

        // --------------------------------------------
        // ✅ 2. EXPORT PDF HANDLING
        // --------------------------------------------
        if (endpoint === "export-pdf") {
            output.innerHTML = `
                <p>📄 PDF Generated Successfully</p>

                <a href="${data.file_url}" target="_blank" 
                   style="color:#38bdf8;font-size:18px;">
                    🔗 Click here to download PDF
                </a>
            `;
            return;
        }

        // --------------------------------------------
        // ✅ 3. ALL OTHER API RESPONSES (INFO, FULL, LIST)
        // --------------------------------------------
        output.textContent = JSON.stringify(data, null, 2);

    } catch (error) {
        output.textContent = "❌ Failed to fetch. Check backend or URL.";
    }
});
