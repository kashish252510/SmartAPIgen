const API_BASE = "http://127.0.0.1:8000/api/v1";

document.addEventListener("DOMContentLoaded", () => {
  initLogin();
  initSignup();
  initDashboard();
});

function initLogin() {
  const loginForm = document.getElementById("loginForm");
  if (!loginForm) return;

  loginForm.addEventListener("submit", (event) => {
    event.preventDefault();
    localStorage.setItem("loggedIn", "true");
    window.location.href = "../dashboard/index.html";
  });
}

function initSignup() {
  const signupForm = document.getElementById("signupForm");
  if (!signupForm) return;

  signupForm.addEventListener("submit", (event) => {
    event.preventDefault();
    const password = document.getElementById("signupPassword").value.trim();
    const confirm = document.getElementById("signupConfirm").value.trim();

    if (password !== confirm) {
      alert("Passwords do not match. Please confirm and try again.");
      return;
    }

    alert("Account created! Please log in to continue.");
    window.location.href = "login.html";
  });
}

function initDashboard() {
  const fetchBtn = document.getElementById("fetchBtn");
  if (!fetchBtn) return;

  enforceAuth();
  const logoutBtn = document.getElementById("logoutBtn");
  logoutBtn?.addEventListener("click", () => {
    localStorage.removeItem("loggedIn");
    window.location.href = "../auth/login.html";
  });

  fetchBtn.addEventListener("click", handleApiRequest);
}

function enforceAuth() {
  if (localStorage.getItem("loggedIn") !== "true") {
    window.location.href = "../auth/login.html";
  }
}

async function handleApiRequest() {
  const urlInput = document.getElementById("urlInput");
  const endpointSelect = document.getElementById("endpointSelect");
  const outputContent = document.getElementById("outputContent");

  const targetUrl = urlInput.value.trim();
  const endpoint = endpointSelect.value;

  if (!targetUrl || !targetUrl.startsWith("http")) {
    outputContent.innerHTML = `<p class="error">Please enter a valid URL starting with http(s)://</p>`;
    return;
  }

  outputContent.innerHTML = `<p class="loading">Processing request...</p>`;

  try {
    const response = await fetch(
      `${API_BASE}/${endpoint}?url=${encodeURIComponent(targetUrl)}`
    );

    if (!response.ok) {
      throw new Error("Backend error");
    }

    const payload = await response.json();

    if (endpoint === "screenshot") {
      renderScreenshot(outputContent, payload);
      return;
    }

    if (endpoint === "export-pdf") {
      renderPdfLink(outputContent, payload);
      return;
    }

    renderJson(outputContent, payload);
  } catch (error) {
    outputContent.innerHTML = `<p class="error">Request failed. Check the URL or ensure the backend is running.</p>`;
  }
}

function renderScreenshot(container, data) {
  container.innerHTML = `
    <p class="success">Screenshot captured successfully.</p>
    <img src="${data.image_url}" alt="Website screenshot" class="preview-img" />
    <button class="primary-btn download-btn" type="button">Download image</button>
  `;

  container.querySelector(".download-btn").addEventListener("click", () => {
    window.open(data.image_url, "_blank");
  });
}

function renderPdfLink(container, data) {
  container.innerHTML = `
    <p class="success">PDF generated successfully.</p>
    <a class="pdf-link" href="${data.file_url}" target="_blank" rel="noopener">Download PDF ↗</a>
  `;
}

function renderJson(container, data) {
  const formatted = JSON.stringify(data, null, 2);
  container.innerHTML = `<pre>${syntaxHighlight(formatted)}</pre>`;
}

function syntaxHighlight(json) {
  return json
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    .replace(
      /("(\\u[a-zA-Z0-9]{4}|\\[^u]|[^\\"])*"(?:\s*:)?|\b(true|false|null)\b|-?\d+(?:\.\d+)?(?:[eE][+\-]?\d+)?)/g,
      (match) => {
        let cls = "json-number";
        if (/^"/.test(match)) {
          cls = /:$/.test(match) ? "json-key" : "json-string";
        } else if (/true|false/.test(match)) {
          cls = "json-boolean";
        } else if (/null/.test(match)) {
          cls = "json-null";
        }
        return `<span class="${cls}">${match}</span>`;
      }
    );
}
