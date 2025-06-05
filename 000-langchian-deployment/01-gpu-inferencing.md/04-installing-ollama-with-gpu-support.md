Great! Let’s move on to:

---

## 🔹 **2.2.2 Installing Ollama with GPU Support (NVIDIA CUDA)**

---

### ✅ 1. What is This Step?

This step explains how to **install Ollama** so that it:
- Runs locally
- Can use **GPU acceleration** (NVIDIA CUDA)
- Supports models like `mistral`, `llama2`, `codellama`, etc.

Ollama uses **llama.cpp** under the hood, which supports GPU via CUDA (on NVIDIA cards).

---

### ✅ 2. Why Do We Need GPU Support?

Without GPU:
- Inference is **very slow** (especially for larger models)
- You may run into **RAM/memory errors**
- Response times can be impractical for production

With GPU:
- You get **10x–30x speedups**
- Lower CPU load and better performance

---

### ✅ 3. When to Install with GPU?

Install GPU support:
- ✅ Before running large models like `mistral`, `llama2`, or `codellama`
- ✅ If you're doing **production RAG**, **chatbots**, or **batch embedding**
- ❌ Skip GPU if you're only testing with small models like `tinyllama`

---

### ✅ 4. Where is This Installed?

You install Ollama:
- On your **host machine** (Linux, Windows, macOS)
- Not inside Docker (we’ll discuss Docker vs host setup later)

> Note: Ollama’s GPU support is available on **Linux** and **Windows with WSL + CUDA**

---

### ⚙️ Steps to Install Ollama (GPU Support)

#### ✅ Step 1: Check GPU Compatibility

1. You need an **NVIDIA GPU**
2. Install **CUDA toolkit** (minimum CUDA 11.8 or 12.1 recommended)
3. Install **latest NVIDIA drivers**

🧪 Test:
```bash
nvidia-smi
```

You should see GPU info and processes.

---

#### ✅ Step 2: Install Ollama

🖥️ For **Windows (WSL2)**:
```bash
winget install Ollama.Ollama
```
Or visit: [https://ollama.com/download](https://ollama.com/download)

🧠 Make sure your **WSL2 distro has CUDA** installed (`nvidia-smi` should work in WSL terminal)

---

🖥️ For **Linux**:
```bash
curl -fsSL https://ollama.com/install.sh | sh
```

> This installs Ollama with GPU support (auto-detects CUDA via `llama.cpp`)

---

### ✅ Optional: Run Ollama as a Service

Start the Ollama background server:
```bash
ollama serve
```

🧪 Test it:
```bash
ollama run mistral
```

If all works, you’ll see:
```
>>> Hello!
<< Hi there! How can I help you?
```

---

### 📌 GPU vs CPU Test

Use `--num-ctx` and `--num-gpu-layers` to control GPU usage:
```bash
OLLAMA_NUM_GPU_LAYERS=35 ollama run mistral
```

---

### 📋 Summary Table

| Aspect                  | Explanation                                                                   |
|--------------------------|-------------------------------------------------------------------------------|
| What is it?              | Installing Ollama with GPU (CUDA) support for fast model inference            |
| Why needed?              | To run large models smoothly and accelerate inference                         |
| When to install GPU?     | Before any serious embedding, generation, or local LLM app                    |
| Where to install?        | On host system (Linux or WSL2 on Windows), not inside Docker                  |
| Key command (Linux)      | `curl -fsSL https://ollama.com/install.sh \| sh`                              |
| Key command (Windows)    | `winget install Ollama.Ollama`                                                |
| Test GPU                 | Run `nvidia-smi` to check CUDA setup                                          |

---
