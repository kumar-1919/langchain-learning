Awesome! Let’s now complete the Ollama GPU setup section with:

---

## 🔹 **2.2.6 Performance Tips and Memory Management (Ollama)**

---

### ✅ 1. What Is This?

This topic focuses on:

* **Optimizing Ollama for GPU/CPU performance**
* Managing **memory usage** and **context sizes**
* Avoiding common **slowdowns** or **crashes** in production setups

---

### ✅ 2. Why Do We Need This?

Because:

* Running large models can **overload RAM or VRAM**
* Ollama may **crash or get killed** (especially with long inputs or many threads)
* Efficient tuning helps avoid GPU **OOM (Out-of-Memory)** errors and speeds up inference

---

### ✅ 3. When Should You Apply These Tips?

Apply when:

* You are running **larger models** (7B, 13B)
* You see **slow generation**, **high memory usage**, or **"killed"** errors
* You want stable behavior in **production**

---

### ✅ 4. Where Are These Optimizations Used?

* In **environment variables**
* During **model load**
* While configuring **LangChain parameters**
* In **Dockerfiles** (if Ollama is containerized)

---

### ⚙️ Key Optimization Settings

#### ✅ A. Limit GPU Layers (for Multi-GPU or Low VRAM)

```bash
OLLAMA_NUM_GPU_LAYERS=35 ollama run mistral
```

* Puts **35 layers** on GPU, rest on CPU
* Default varies per model
* Tune for your GPU memory (e.g., 24 for 8GB GPU)

---

#### ✅ B. Increase Context Window

```bash
OLLAMA_NUM_CTX=4096
```

* Default: **2048**
* Some models (like Mistral) support **32K tokens**
* More context = more memory usage

---

#### ✅ C. Control Threads

```bash
OLLAMA_NUM_THREADS=4
```

* Number of CPU threads used for inference
* Set based on available cores
* Helps balance performance vs system load

---

#### ✅ D. Reduce Model Size (Quantization)

Use lighter model formats:

```bash
ollama pull mistral:latest  # default is quantized
```

Or specify:

```bash
ollama pull mistral:Q4_K_M
```

* Smaller quantizations (Q4\_0, Q4\_K\_M) = faster, less RAM
* Trade-off: Lower quality vs smaller size

---

#### ✅ E. Enable Swap Memory (Linux Only)

In `/etc/fstab` or with `fallocate`, enable swap:

```bash
sudo fallocate -l 8G /swapfile
sudo chmod 600 /swapfile
sudo mkswap /swapfile
sudo swapon /swapfile
```

Prevents **crashes** due to full memory during generation or embedding.

---

### 🔥 Pro Tip: Avoid Loading All Documents at Startup

In LangChain-based RAG apps:

* Don't load or embed everything at app startup
* Use **lazy loading**, **pagination**, or **batch embedding**

---

### 📋 Summary Table

| Optimization            | Description                                                    | Default / Tip                |
| ----------------------- | -------------------------------------------------------------- | ---------------------------- |
| `OLLAMA_NUM_GPU_LAYERS` | Number of transformer layers on GPU                            | 0–40 (depends on model)      |
| `OLLAMA_NUM_CTX`        | Token context size                                             | 2048 (can be increased)      |
| `OLLAMA_NUM_THREADS`    | Threads for parallel CPU processing                            | Auto-detect, tune as needed  |
| Quantization level      | Lower = faster, smaller; higher = better output                | `Q4_0`, `Q4_K_M` (balanced)  |
| Swap Memory             | Prevents OOM crash on Linux                                    | Enable at least 4–8 GB swap  |
| Lazy Document Loading   | Prevents memory overload when using large datasets in RAG apps | Use generators or async load |

---

✅ That wraps up **Section 2: Setting up Ollama for GPU Inference**.

Would you like to proceed to **Section 3: Dockerizing LangChain Apps** now?
