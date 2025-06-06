Perfect! Let’s now dive into:

---

## 📘 3.3 – **Key Parameters: `temperature`, `top_p`, `max_tokens`**

---

### 🎯 Goal:

Understand the core generation parameters used in LLMs and how they affect the output. You’ll also learn their definitions, purpose, default/min/max values, and which parameter to tune in what situation.

---

### 📘 Curriculum for 3.3

| Topic                        | Description                                                         |
| ---------------------------- | ------------------------------------------------------------------- |
| ✅ What are these parameters? | Explanation of `temperature`, `top_p`, `max_tokens`                 |
| 🔍 Why do we need them?      | To control randomness, creativity, length, and quality of responses |
| 📅 When to tune which?       | Use cases for changing each parameter                               |
| 🌍 Where to use them?        | In LLM calls inside chains, agents, chat apps, RAG, etc.            |
| 🧪 Code Examples             | Working examples showing their effect                               |
| ⚙️ Parameter Reference       | Default, min, max, required or optional                             |
| 🧠 Technical Terms           | Sampling, Nucleus Sampling, Token Budget, Truncation                |
| 📄 Summary Table             | One-liner comparison with tuning tips                               |

---

## 🧠 What are These Parameters?

---

### 1️⃣ `temperature`

Controls **randomness** of the model’s output.

* **Low (`0.0`)** = more deterministic, focused, repeatable
* **High (`1.0`)** = more creative, varied, random

#### 📘 Default Values:

| Model Type | Default | Min   | Max   |
| ---------- | ------- | ----- | ----- |
| OpenAI     | `0.7`   | `0.0` | `2.0` |
| Anthropic  | `0.7`   | `0.0` | `1.0` |
| Ollama     | `0.8`   | `0.0` | `1.0` |

---

### 2️⃣ `top_p` (a.k.a **nucleus sampling**)

Controls the **probability mass** from which the next token is sampled.

* `top_p = 1.0` → consider all tokens (default)
* `top_p = 0.5` → only top tokens whose cumulative probability ≤ 50%

🧠 If both `temperature` and `top_p` are used:
They interact. Best to **tune only one** (usually `temperature`).

#### 📘 Default Values:

| Model Type | Default | Min   | Max   |
| ---------- | ------- | ----- | ----- |
| OpenAI     | `1.0`   | `0.0` | `1.0` |
| Anthropic  | `1.0`   | `0.0` | `1.0` |
| Ollama     | `1.0`   | `0.0` | `1.0` |

---

### 3️⃣ `max_tokens`

Defines the **maximum number of tokens** in the **output**.

* If you want a short summary → `max_tokens=50`
* For story generation → `max_tokens=500+`
* Helps **limit cost** and **control response size**

#### 📘 Default & Range:

| Model Type | Default (varies) | Max Tokens (based on context window) |
| ---------- | ---------------- | ------------------------------------ |
| GPT-4      | \~128 tokens     | 8192 / 128k (model dependent)        |
| Claude     | \~256 tokens     | Up to 200,000                        |
| Ollama     | Depends on model | Usually 2048–8192                    |

---

## 🧪 Code Examples

Let’s test these using `Ollama`.

### ✅ Example: `temperature` changes

```python
from langchain_community.chat_models import ChatOllama
from langchain_core.messages import HumanMessage

prompt = [HumanMessage(content="Write a poem about a cat")]

# Deterministic response
llm_0 = ChatOllama(model="llama3", temperature=0.0)
print("0.0 Temp:", llm_0.invoke(prompt).content)

# Creative response
llm_1 = ChatOllama(model="llama3", temperature=1.0)
print("1.0 Temp:", llm_1.invoke(prompt).content)
```

### ✅ Example: `top_p`

```python
llm = ChatOllama(model="llama3", top_p=0.5)
print(llm.invoke([HumanMessage(content="Describe the moon.")]).content)
```

### ✅ Example: `max_tokens`

```python
llm = ChatOllama(model="llama3", max_tokens=20)
print(llm.invoke([HumanMessage(content="Explain quantum mechanics")]).content)
```

---

## 🔍 Why Use These?

| Parameter     | Why You Need It                                             |
| ------------- | ----------------------------------------------------------- |
| `temperature` | Add creativity or make outputs more reliable                |
| `top_p`       | Filter token options to limit weird or rare choices         |
| `max_tokens`  | Save cost, limit answer length, prevent overflow/truncation |

---

## 📅 When to Use Which?

| Situation             | Best Parameter Strategy                |
| --------------------- | -------------------------------------- |
| Writing legal answers | `temperature=0.0`, `top_p=1.0`         |
| Creative storytelling | `temperature=0.9`, `top_p=1.0`         |
| Haikus or poetry      | `temperature=1.0`, `top_p=0.95`        |
| Summary generation    | `max_tokens=50-100`, `temperature=0.3` |
| General chatbots      | `temperature=0.7`, `max_tokens=256`    |

---

## 🧠 Technical Terms

| Term                 | Meaning                                                              |
| -------------------- | -------------------------------------------------------------------- |
| **Token**            | Word or word part; e.g., “ChatGPT” = 1 token, “Chat GPT” = 2 tokens  |
| **Sampling**         | Model chooses next word from possible options based on probabilities |
| **Nucleus Sampling** | Another term for `top_p`, i.e., sample from top % probability mass   |
| **Truncation**       | Model cuts output if token limit is reached                          |
| **Prompt Budget**    | Combined input + output token limit based on model's context window  |

---

## 📄 Summary Table

| Parameter     | Default | Range          | Purpose                              | Tune When                        |
| ------------- | ------- | -------------- | ------------------------------------ | -------------------------------- |
| `temperature` | `0.7`   | `0.0 – 2.0`    | Controls randomness/creativity       | You want creative or safe output |
| `top_p`       | `1.0`   | `0.0 – 1.0`    | Filters token choices by probability | You want focused response        |
| `max_tokens`  | Varies  | Depends on LLM | Controls output length               | You want short/long answers      |

---

✅ This wraps up all about **key generation parameters** in LangChain-supported LLMs.

Would you like to move on to **3.4 – Synchronous vs Asynchronous Calls**, or do you want a quick downloadable summary of what we've done so far?
