Great! Let’s continue with:

---

## 🔹 **2.2.3 Pulling GPU-Compatible Models in Ollama**

---

### ✅ 1. What Is This Step?

This step is about:

* Downloading LLMs that are **compatible with GPU**
* Making sure Ollama pulls models in the **GGUF format** optimized for inference
* Ensuring models run on **CUDA-enabled GPU** if available

---

### ✅ 2. Why Do We Need to Pull Models?

* 🧠 Ollama doesn’t come with models pre-installed
* You must **pull models manually** using the `ollama pull` command
* Different models have different size versions optimized for CPU or GPU (e.g., 3B, 7B, 13B)

---

### ✅ 3. When Should You Pull GPU-Compatible Models?

* After installing Ollama and verifying CUDA is working
* When you plan to run the model for **chat, embedding, reranking, or RAG**
* Anytime you want to **experiment with a new model** or **upgrade**

---

### ✅ 4. Where Are the Models Stored?

Models are stored in:

```
~/.ollama/models/
```

You can list all pulled models:

```bash
ollama list
```

They are stored locally, and Ollama **does not re-download** them each time.

---

### ⚙️ Pulling a Model (Command)

```bash
ollama pull mistral
```

This downloads the default quantized GGUF version of Mistral (usually `q4_0` or `q4_K_M`).

Other examples:

```bash
ollama pull llama2
ollama pull codellama
ollama pull phi
```

🔍 To view available models:
Visit [https://ollama.com/library](https://ollama.com/library)

---

### 🧪 Test: Run the Model

```bash
ollama run mistral
```

If everything is okay, Ollama will use the GPU automatically.

Behind the scenes:

* Uses **llama.cpp** with GPU acceleration
* Loads the GGUF model file
* Streams output through `localhost:11434`

---

### ⚠️ Tip: Choose GPU-Friendly Quantization

Ollama defaults to **quantized formats**. For best GPU usage:

* Use `q4_K_M` or higher
* Use `OLLAMA_NUM_GPU_LAYERS` to shift layers to GPU:

```bash
OLLAMA_NUM_GPU_LAYERS=35 ollama run mistral
```

---

### 📌 Optional: Create Custom Model

You can create your own model from a base:

```bash
ollama create mymodel -f Modelfile
```

Sample `Modelfile`:

```
FROM mistral
SYSTEM You are a helpful AI assistant.
```

Then:

```bash
ollama run mymodel
```

---

### 📋 Summary Table

| Aspect        | Explanation                                                    |
| ------------- | -------------------------------------------------------------- |
| What is it?   | Downloading GGUF format LLMs for local inference               |
| Why needed?   | Ollama doesn’t include models by default; pulling is necessary |
| When to pull? | After installation and before LangChain integration            |
| Where stored? | `~/.ollama/models/`                                            |
| Common models | `mistral`, `llama2`, `phi`, `codellama`, `dolphin-mixtral`     |
| GPU tips      | Use quantized formats + set `OLLAMA_NUM_GPU_LAYERS`            |

---

✅ Shall we proceed to **2.2.4 Running Ollama Inside vs Outside Docker (pros and cons)**?
