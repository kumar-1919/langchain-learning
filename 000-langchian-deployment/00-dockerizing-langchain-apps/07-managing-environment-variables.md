Great! Let’s move on to:

---

## 🌱 **1.4 Managing Environment Variables in Docker**

---

### ✅ What Are Environment Variables?

**Environment Variables (env vars)** are key-value pairs used to:

* Store **configuration data** (like API keys, database URLs, or model names)
* Separate config from code (12-Factor App principle)

In Docker, env vars can be:

* Defined inside the Dockerfile
* Passed during container run
* Loaded from a `.env` file

---

### ✅ Why Do We Need Them?

For LangChain apps, env vars are used to:

* Store **API keys** (e.g., OpenAI, HuggingFace, Pinecone)
* Define **config settings** (e.g., model name, DB paths)
* Set **runtime parameters** (e.g., port, debug mode)

Using env vars:

* Makes the app more flexible and secure
* Avoids hardcoding sensitive data into the source code

---

### ✅ When to Use Them?

* When deploying to **multiple environments** (dev, staging, prod)
* When your app uses:

  * `.env` files
  * `.getenv()` or `os.environ.get()`
  * External services requiring secrets (LLM APIs, vector stores)

---

### ✅ Where to Use Them?

You can set env vars in multiple ways:

---

### 🔹 Option 1: In Dockerfile

```dockerfile
ENV MODEL_NAME="nomic-embed-text"
ENV DEBUG=True
```

Use them in Python:

```python
import os
model = os.getenv("MODEL_NAME", "default-model")  # fallback supported
```

---

### 🔹 Option 2: Using `.env` + `docker run --env-file`

**`.env` file**

```
MODEL_NAME=nomic-embed-text
DEBUG=True
```

Run container with:

```bash
docker run --env-file .env -p 5000:5000 langchain-app
```

---

### 🔹 Option 3: CLI with `-e` Flags

```bash
docker run -e MODEL_NAME=nomic-embed-text -e DEBUG=True -p 5000:5000 langchain-app
```

---

### 🔐 Best Practices

✅ Don’t hardcode secrets like API keys in Python or Dockerfile
✅ Use `.env` files and `.dockerignore` to avoid leaking secrets
✅ Load variables in code like this:

```python
import os
openai_api_key = os.getenv("OPENAI_API_KEY", "")
```

---

### 📋 Summary Table

| Aspect             | Explanation                                                      |
| ------------------ | ---------------------------------------------------------------- |
| What is it?        | Key-value settings used to configure the app at runtime          |
| Why needed?        | Keeps config flexible and separates code from secrets            |
| When to use?       | Always in multi-env or API-driven apps like LangChain            |
| Where to set them? | Dockerfile, `.env`, or CLI (`-e`)                                |
| Best practice      | Use `.env`, load with `os.getenv()`, and ignore secrets in image |

---

✅ Shall we go to the next section: **1.5 Building and Running the Docker Image**?
