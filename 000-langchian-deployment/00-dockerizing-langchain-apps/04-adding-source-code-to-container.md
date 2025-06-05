Perfect! Let’s move to:

---

## 🔹 **1.2.3 Adding App Code**

---

### ✅ What is This Step?

This step involves **copying your source code files** from your local machine into the Docker container.

This typically includes:

* Main Python app (`main.py`)
* Utility modules (`utils.py`, etc.)
* Templates, static files (if any)
* Vector DB folder (if you're persisting locally)
* Any other project files needed to run the app

---

### ✅ Why Do We Need This Step?

* Your app logic must be **inside the container** so Docker can run it
* Without this step, the container won’t know how to execute your code

---

### ✅ When to Use It?

* Always include this step after setting up the base image and installing dependencies
* Must be done **before** the `CMD` or `ENTRYPOINT` (final command to run app)

---

### ✅ Where in Dockerfile?

Right after installing dependencies.

---

### ✅ How to Do It?

Use the `COPY` or `ADD` instruction.

```dockerfile
# Copy all source code into the container
COPY . .
```

You can also be more specific:

```dockerfile
COPY app/ /app
COPY config.yaml /app/config.yaml
COPY entrypoint.sh /entrypoint.sh
```

If you used `WORKDIR /app`, files will be copied into that path.

---

### 📁 Example Project Structure

```
my-langchain-app/
├── app/
│   ├── main.py
│   └── utils.py
├── requirements.txt
├── Dockerfile
├── .dockerignore
└── README.md
```

**Dockerfile:**

```dockerfile
FROM python:3.10-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy app code
COPY . .
```

---

### 📦 Tip: Use `.dockerignore`

To avoid copying unnecessary files:

**.dockerignore**

```
__pycache__/
*.pyc
.env
*.md
.vscode/
```

---

### 📋 Summary Table

| Aspect               | Explanation                                                    |
| -------------------- | -------------------------------------------------------------- |
| What is it?          | Step to copy your app code into the Docker container           |
| Why needed?          | App won’t work unless your source files are available in image |
| When to use?         | After installing dependencies, before setting CMD              |
| Where in Dockerfile? | After `RUN pip install...`, use `COPY . .`                     |
| Best practice        | Use `.dockerignore` to skip unwanted files                     |

---

✅ Shall we move to **1.2.4 Exposing Ports & Running the App**?