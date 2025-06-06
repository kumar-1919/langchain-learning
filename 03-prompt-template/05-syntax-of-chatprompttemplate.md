Great! Let's move on to:

---

## 📘 4.2.2 – Syntax and Usage of `ChatPromptTemplate`

(Updated for Latest LangChain Version)

---

### 🎯 Goal:

Learn the **syntax**, **parameters**, and how to **build and use `ChatPromptTemplate`** to work with chat-based LLMs like `ChatOpenAI`, `ChatOllama`, etc.

---

## 🧱 Syntax Overview

```python
ChatPromptTemplate.from_messages(
    messages: List[Tuple[str, str]]  # or List[BaseMessagePromptTemplate]
)
```

OR using message-specific classes:

```python
from langchain.prompts import ChatPromptTemplate, SystemMessagePromptTemplate, HumanMessagePromptTemplate

ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(...),
    HumanMessagePromptTemplate.from_template(...)
])
```

---

### 📌 Parameters

| Parameter  | Type                                                     | Required | Description                                          |
| ---------- | -------------------------------------------------------- | -------- | ---------------------------------------------------- |
| `messages` | List\[Tuple\[str, str]] OR List\[PromptMessageTemplates] | ✅ Yes    | Sequence of messages representing the prompt history |

📝 Valid roles: `"system"`, `"human"`, `"ai"`

---

### ✅ Simple Syntax – Tuple Style

```python
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant."),
    ("human", "Translate the following to French: {sentence}")
])

print(prompt.format_messages(sentence="How are you?"))
```

🟢 Output:

```
[SystemMessage(content='You are a helpful assistant.'),
 HumanMessage(content='Translate the following to French: How are you?')]
```

---

### ✅ Advanced Syntax – Template Objects

```python
from langchain.prompts import ChatPromptTemplate, SystemMessagePromptTemplate, HumanMessagePromptTemplate

system_msg = SystemMessagePromptTemplate.from_template("You are a translator bot.")
human_msg = HumanMessagePromptTemplate.from_template("Translate this: {text}")

chat_prompt = ChatPromptTemplate.from_messages([system_msg, human_msg])
messages = chat_prompt.format_messages(text="I love pizza.")
```

🟢 Output:

```
[SystemMessage(content='You are a translator bot.'),
 HumanMessage(content='Translate this: I love pizza.')]
```

---

## 🧠 Use with Chat LLM

```python
from langchain.chat_models import ChatOpenAI

chat = ChatOpenAI(model="gpt-3.5-turbo")

response = chat.invoke(messages)
print(response.content)
```

---

## 🔄 Common Method: `format_messages()`

| Method                       | Description                                                |
| ---------------------------- | ---------------------------------------------------------- |
| `.format_messages(**kwargs)` | Fills all placeholders and returns list of message objects |

---

## ⚠️ Error Handling

| Error                     | Cause                                           | Fix                                          |
| ------------------------- | ----------------------------------------------- | -------------------------------------------- |
| `Missing input variable`  | Forgot to pass variable to `.format_messages()` | Add required keyword argument                |
| `Invalid role type`       | Role name not in `["system", "human", "ai"]`    | Fix role name                                |
| `List index out of range` | Empty or malformed message list                 | Ensure message tuples or objects are correct |

---

## ✅ Summary Table

| Feature           | Description                                                |
| ----------------- | ---------------------------------------------------------- |
| Class             | `ChatPromptTemplate`                                       |
| Role Support      | `system`, `human`, `ai`                                    |
| Output            | `List[BaseMessage]`                                        |
| Main Method       | `.from_messages([...])`                                    |
| Formatting Method | `.format_messages(**kwargs)`                               |
| LLM Compatibility | All chat-based models: GPT-4, Claude, Ollama (chat models) |

---

Would you like to continue to:
📘 **4.2.3 – Use Cases of `ChatPromptTemplate`**?
