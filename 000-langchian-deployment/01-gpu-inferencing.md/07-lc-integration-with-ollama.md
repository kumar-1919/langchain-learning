Awesome! Let’s continue with:

---

## 🔹 **2.2.5 LangChain Integration with Ollama**

---

### ✅ 1. What Is This?

This topic explains:

* How to **use Ollama as an LLM or Embedding model in LangChain**
* How to configure it to connect with **Ollama running on host or Docker**
* How to use it for **generation** or **embedding** in your apps

---

### ✅ 2. Why Do We Need This?

* LangChain supports **many LLM backends** (OpenAI, HuggingFace, Ollama, etc.)
* We need to explicitly tell it to **use Ollama**, and **where it’s hosted**
* Allows running full **RAG pipelines**, **tools**, **agents**, and **chatbots** without cloud APIs

---

### ✅ 3. When to Use This Integration?

Use when:

* You have **Ollama running locally** or in a container
* You want to run **generation or embedding** locally
* You want to avoid OpenAI/HuggingFace APIs

---

### ✅ 4. Where Is This Used in LangChain?

LangChain uses Ollama in:

* `ChatOllama` → for **chat models**
* `Ollama` → for **completion-style models**
* `OllamaEmbeddings` → for **document embeddings**

You can plug these into:

* **RAG pipelines**
* **Agents**
* **Q\&A chains**
* **Custom LangChain workflows**

---

### ⚙️ How to Use Ollama in LangChain (Code Example)

#### ✅ A. For Text Generation (e.g., Q\&A, Chatbot)

```python
from langchain_community.llms import Ollama

llm = Ollama(
    model="mistral",  # Or "phi", "llama2", etc.
    base_url="http://localhost:11434"  # or "http://host.docker.internal:11434"
)

response = llm.invoke("What is LangChain?")
print(response)
```

---

#### ✅ B. For Chat Model (Memory, Streaming, Agents)

```python
from langchain_community.chat_models import ChatOllama

chat_model = ChatOllama(
    model="mistral", 
    base_url="http://localhost:11434"
)

response = chat_model.invoke("Summarize this: LangChain is...")
print(response.content)
```

---

#### ✅ C. For Embeddings (RAG Setup)

```python
from langchain_community.embeddings import OllamaEmbeddings

embedding = OllamaEmbeddings(
    model="nomic-embed-text",
    base_url="http://localhost:11434"
)

vec = embedding.embed_query("What is Retrieval Augmented Generation?")
print(vec[:5])  # preview of vector
```

---

### 🔍 Parameter Breakdown (For `Ollama()` and `ChatOllama()`)

| Parameter     | Description                               | Required | Default                  |
| ------------- | ----------------------------------------- | -------- | ------------------------ |
| `model`       | Name of the model (e.g., mistral, llama2) | ✅ Yes    | None                     |
| `base_url`    | Host URL of Ollama API                    | ❌ No     | `http://localhost:11434` |
| `temperature` | Sampling randomness (0 = deterministic)   | ❌ No     | `0.8`                    |
| `top_p`       | Nucleus sampling limit (range 0–1)        | ❌ No     | `1.0`                    |
| `stop`        | List of stop sequences                    | ❌ No     | None                     |
| `num_ctx`     | Context length in tokens                  | ❌ No     | 2048 or model-specific   |

---

### 🔁 Optional: Streaming with Ollama

```python
response = llm.stream("Write a poem about clouds")
for chunk in response:
    print(chunk, end="")
```

---

### 📋 Summary Table

| Aspect           | Details                                                                      |
| ---------------- | ---------------------------------------------------------------------------- |
| What is it?      | Using Ollama models inside LangChain for generation/embedding                |
| Why use it?      | Local, private, fast model inference for LangChain apps                      |
| When to use?     | Any time you want cloud-free LLMs in RAG, QA, tools, agents                  |
| Where used?      | LLMs (`Ollama`), Chat models (`ChatOllama`), Embeddings (`OllamaEmbeddings`) |
| Required param   | `model` (e.g., `"mistral"`)                                                  |
| Connection point | `base_url="http://host.docker.internal:11434"` if inside Docker              |

---

✅ Shall we move on to the last sub-subtopic: **2.2.6 Performance Tips and Memory Management**?
