

🚀 **SmartAPI Gen**
### **Intelligence Behind Every Endpoint**

SmartAPI Gen is an AI-powered system that converts **any website** into **structured, ready-to-use API endpoints**—including JSON, screenshots, and PDFs—instantly.

This project combines a polished frontend dashboard with a powerful backend engine to let developers extract data, generate APIs, and automate web intelligence workflows in real time.

---

# ✨ **Features**

### 🔗 **Website → API Conversion**

Turn any public URL into:

* Clean JSON data
* Metadata (title, description, canonical URL)
* Favicon links
* Auto-structured fields

### 🖼️ **Screenshot Engine**

Generate:

* Full-page screenshots
* Device-scaled previews
* Retina-quality images

### 📄 **PDF Export Engine**

Convert any webpage into:

* Pixel-perfect PDF exports
* Shareable documentation snapshots

### 🛠️ **Live API Control Center**

The dashboard provides:

* URL input
* Endpoint selection
* Live JSON preview
* Downloadable media (screenshots & PDFs)

### ⚡ **Backend Automation**

* Fast web extraction
* AI-assisted structuring
* Clean response formatting
* Supports multiple output modes

---

# 🧰 **Tech Stack**

### **Backend**

* Python (FastAPI)
* Uvicorn (ASGI server)
* Playwright / Requests for extraction
* PIL / PyPDF for media generation

### **Frontend**

* HTML + CSS + Vanilla JS
* Custom dark-mode SaaS UI
* Responsive glass-style components

### **Tools**

* Axios / Fetch API
* Postman / Thunder Client
* dotenv for environment config

---

# 📁 **Project Structure**

```
SmartAPIgen/
│── app/                  # Backend API logic
│── frontend/             # Full frontend dashboard UI
│── static/saved_files/   # Output screenshots & PDFs
│── tests/                # Backend tests
│── README.md
```

---

# ⚙️ **Installation & Setup**

### **1. Clone the repository**

```bash
git clone https://github.com/kashish252510/SmartAPIgen.git
cd SmartAPIgen
```

---

## 🖥️ **Backend Setup (FastAPI)**

### **Install dependencies**

```bash
pip install -r requirements.txt
```

### **Run backend server**

```bash
python -m uvicorn app.main:app --reload
```

Server runs at:

```
http://127.0.0.1:8000
```

---

## 🎨 **Frontend Setup**

Go to the frontend folder:

```bash
cd frontend
```

### Run local static server:

```bash
npx serve .
```

or using Python:

```bash
python -m http.server 5500
```

Frontend opens at:

```
http://localhost:5500
```

---

# 🧪 **API Example Usage**

### **Extract info**

```bash
GET /extract?url=https://example.com
```

### **Screenshot**

```bash
GET /screenshot?url=https://example.com
```

### **PDF Export**

```bash
GET /pdf?url=https://example.com
```

---

# 🖥️ **Dashboard Preview**

The dashboard provides:

* URL input
* Endpoint selector
* Generate button
* Live JSON output
* Screenshot preview
* PDF download link
  All wrapped in a premium dark-glass UI.

---

# 🛡️ **Security Notes**

SmartAPI Gen:

* Blocks private/internal network URLs
* Sanitizes all inputs
* Limits page execution time
* Prevents unauthorized JavaScript execution

---

# 🤝 **Contributing**

Pull requests and feature suggestions are welcome.
Open an issue and let's build together!

---

# 📜 **License**

MIT License — Free to use, modify, and distribute.

---


