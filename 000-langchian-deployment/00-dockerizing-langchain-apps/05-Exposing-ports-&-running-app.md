Excellent! Let's go to the final step of Dockerfile creation:

---

## 🔹 **1.2.4 Exposing Ports & Running the App**

---

### ✅ What is This Step?

This step does **two things**:

1. **Expose** the port your app will listen on (e.g., 5000 for Flask)
2. **Run** the app using a command like `python main.py` or `gunicorn app:app`

---

### ✅ Why Do We Need It?

* **Expose** makes sure Docker knows which port the app will use so you can map it to your host machine.
* **CMD** or **ENTRYPOINT** defines **how to start your application** when the container runs.

Without this, your app won’t start properly inside the container.

---

### ✅ When to Use?

Use it:

* After copying all code and installing dependencies
* As the **final section** of your Dockerfile

---

### ✅ Where to Use in Dockerfile?

Near the bottom, just before the end.

---

### ✅ Syntax

#### 🔓 `EXPOSE` (optional but recommended)

```dockerfile
EXPOSE 5000
```

This doesn't publish the port automatically but is useful for documentation and tools like Docker Compose.

#### 🚀 `CMD` or `ENTRYPOINT`

To run your Flask app:

```dockerfile
CMD ["python", "app/main.py"]
```

Or with Gunicorn (better for production):

```dockerfile
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "app.main:app"]
```

---

### 🧪 Full Dockerfile Example (Putting it All Together)

```dockerfile
# Dockerfile
FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["python", "app/main.py"]
```

---

### 📋 Summary Table

| Aspect             | Explanation                                                    |
| ------------------ | -------------------------------------------------------------- |
| What is it?        | Expose app port + define how to start the app inside container |
| Why needed?        | App won’t run unless Docker knows how to start it              |
| When to use?       | Final step in the Dockerfile                                   |
| Where to place it? | At the end of the Dockerfile                                   |
| Best practices     | Use `CMD` for simple runs, `gunicorn` for production apps      |

---

✅ That completes the entire subtopic **1.2 Writing a Dockerfile**.

Would you like a **summary table for section 1.2** before we continue to **1.3 Using `.dockerignore`**?
