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
  
      if (!response.ok) {
        throw new Error("Backend error");
      }
  
      const data = await response.json();
      output.textContent = JSON.stringify(data, null, 2);
  
    } catch (error) {
      output.textContent = "❌ Failed to fetch. Check backend or URL.";
    }
});
