Perfect! Let’s move to:

---

## 📘 4.2.1 – What is `ChatPromptTemplate`?

---

### 🎯 Goal:

Understand what `ChatPromptTemplate` is, how it differs from `PromptTemplate`, and where it fits in building **chat-style prompts** for LLMs that support messages (like OpenAI, Anthropic, Ollama, etc.).

---

## 🔍 What is `ChatPromptTemplate`?

`ChatPromptTemplate` is a LangChain class that lets you **construct multi-message prompts** for chat-based LLMs.

Unlike `PromptTemplate`, which returns a **single string**, `ChatPromptTemplate` builds a **structured list of messages** like:

* System message
* Human message
* AI message
* Function call, tool call (advanced)

This is ideal for LLMs like:

* OpenAI GPT-4
* Anthropic Claude
* Ollama (chat-capable models like `llama3`)
* HuggingFace chat interfaces

---

## 🧠 Technical Terms Used

| Term            | Meaning                                                               |
| --------------- | --------------------------------------------------------------------- |
| System message  | Sets the behavior or personality of the assistant                     |
| Human message   | Represents the user’s input                                           |
| AI message      | Represents the assistant’s previous response (optional)               |
| MessageTemplate | A single message (can be system/human/ai) within a ChatPromptTemplate |

---

## ❓Why use `ChatPromptTemplate`?

* To mimic **chat history** in a structured way
* Required by chat models like GPT-4, Claude, Llama3, etc.
* Helps maintain **role separation**: system vs human vs assistant
* Needed for **function calling** and **multi-turn memory**

---

## ⚙️ Class Signature

```python
ChatPromptTemplate.from_messages(
    messages: List[BaseMessagePromptTemplate]
)
```

You can use specific message templates like:

```python
from langchain.prompts import (
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
    AIMessagePromptTemplate,
)
```

---

## ✅ Default values:

There are **no default messages** — you must define at least a human or system message.

---

## ✅ Example: Simple ChatPromptTemplate

```python
from langchain.prompts import ChatPromptTemplate

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant."),
    ("human", "What is the capital of {country}?")
])

formatted_prompt = prompt.format_messages(country="India")
for message in formatted_prompt:
    print(message)
```

🟢 Output (Message objects):

```
SystemMessage(content='You are a helpful assistant.')
HumanMessage(content='What is the capital of India?')
```

These messages are passed to the chat LLMs as a **chat history**.

---

### ✅ Difference from PromptTemplate

| Feature           | PromptTemplate     | ChatPromptTemplate                         |
| ----------------- | ------------------ | ------------------------------------------ |
| Output            | `str`              | `List[BaseMessage]`                        |
| Use case          | Single-turn prompt | Multi-turn/chat-style prompting            |
| LLM Compatibility | Basic LLMs         | Chat LLMs (OpenAI, Anthropic, Ollama chat) |
| Roles             | ❌ None             | ✅ system, human, ai roles supported        |

---

## ✅ Summary Table

| Feature           | Value                                             |
| ----------------- | ------------------------------------------------- |
| Class Name        | `ChatPromptTemplate`                              |
| Source Method     | `.from_messages()`                                |
| Output            | List of `BaseMessage` objects                     |
| Message Types     | `system`, `human`, `ai`                           |
| Used with         | Chat-based LLMs like GPT-4, Claude, LLaMA3, etc.  |
| Required Messages | At least one human/system message                 |
| Compatible With   | `ChatOpenAI`, `ChatAnthropic`, `ChatOllama`, etc. |

---

Would you like to proceed to:

📘 **4.2.2 – Syntax and Usage of ChatPromptTemplate**?
