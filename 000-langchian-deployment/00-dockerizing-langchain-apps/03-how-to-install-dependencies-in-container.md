Great! Let’s move on to:

---

## 🔹 **1.2.2 Installing Dependencies**

---

### ✅ What is This Step?

In this step, you tell Docker which **Python packages and system-level libraries** your LangChain app needs to run.

Dependencies include:
- Python packages (`langchain`, `chromadb`, `flask`, etc.)
- System libraries (`gcc`, `libc`, `curl`, etc. – if required)

---

### ✅ Why Do We Need This Step?

- To make sure all the required libraries are installed inside the container
- Without it, the app will crash with `ModuleNotFoundError`

---

### ✅ When to Use This?

- **Every time** your app uses external Python libraries or system tools
- Especially important for:
  - LangChain modules (`langchain`, `chromadb`)
  - Server frameworks (`flask`, `fastapi`)
  - Parsing, NLP, vector search (`tiktoken`, `sentence-transformers`)

---

### ✅ Where to Use in Dockerfile?

After specifying the base image.

---

### ✅ How to Do It? (With Examples)

#### 📦 Option 1: Use `requirements.txt`

Best practice!

```dockerfile
# Dockerfile
FROM python:3.10-slim

# Set work directory
WORKDIR /app

# Copy requirements file
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt
```

**`requirements.txt`:**
```
langchain
chromadb
flask
tiktoken
```

#### ⚙️ Option 2: Inline Install (Not Recommended for Production)

```dockerfile
RUN pip install --no-cache-dir langchain chromadb flask tiktoken
```

---

### 🧠 Pro Tip: System Dependencies

Some packages (like FAISS or sentence-transformers) need system tools.

You can add system-level dependencies like:

```dockerfile
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*
```

---

### 📋 Summary Table

| Aspect              | Explanation                                                       |
|----------------------|-------------------------------------------------------------------|
| What is it?          | Step to install Python and system dependencies                    |
| Why needed?          | Required to run LangChain, Flask, VectorDBs, etc.                 |
| When to use?         | Always, before running the app inside Docker                      |
| Where in Dockerfile? | After `FROM` and `WORKDIR`, before copying the source code        |
| Best practice        | Use `requirements.txt` and install with `pip install -r`          |

---

✅ Ready to continue to **1.2.3 Adding App Code**?