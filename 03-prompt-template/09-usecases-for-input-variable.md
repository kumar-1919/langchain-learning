Awesome! Let's continue:

---

## 📘 4.3.3 – Real-World Examples Using Input Variables

---

### 🎯 Goal:

Apply your understanding of input variables through practical, real-world examples using both `PromptTemplate` and `ChatPromptTemplate`.

---

## ✅ Example 1: Dynamic Translation (PromptTemplate)

```python
from langchain.prompts import PromptTemplate

template = PromptTemplate.from_template(
    "Translate this sentence to {language}: {sentence}"
)

output = template.format(language="French", sentence="I love programming.")
print(output)
```

🟢 Output:

```
Translate this sentence to French: I love programming.
```

👨‍💻 **Use Case**: Language learning apps, multi-lingual chatbots.

---

## ✅ Example 2: Email Generator (PromptTemplate)

```python
template = PromptTemplate.from_template(
    "Write a professional email to {client_name} about {subject}."
)

email = template.format(client_name="Mr. Ramesh", subject="the project deadline")
print(email)
```

👨‍💼 **Use Case**: Automated business communication.

---

## ✅ Example 3: Structured Chat Prompt (ChatPromptTemplate)

```python
from langchain.prompts import ChatPromptTemplate

chat_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a customer support bot."),
    ("human", "A customer asked: {question}"),
    ("ai", "Here’s how you should respond: {answer}")
])

formatted_messages = chat_prompt.format_messages(
    question="Where is my order?",
    answer="Apologize and check the tracking number."
)

for msg in formatted_messages:
    print(f"[{msg.type.upper()}] {msg.content}")
```

🟢 Output:

```
[SYSTEM] You are a customer support bot.
[HUMAN] A customer asked: Where is my order?
[AI] Here’s how you should respond: Apologize and check the tracking number.
```

📦 **Use Case**: Call center assistant, customer service LLMs.

---

## ✅ Example 4: Coding Helper Chat (Few-Shot + Variables)

```python
chat_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a Python assistant."),
    ("human", "How to reverse a list in Python?"),
    ("ai", "Use list[::-1] or list.reverse()."),
    ("human", "{new_question}")
])

messages = chat_prompt.format_messages(new_question="How to sort a list?")
```

🧑‍🏫 **Use Case**: Educational tutors or coding bots.

---

## ✅ Example 5: RAG + Retrieved Context (Hybrid Prompt)

```python
ChatPromptTemplate.from_messages([
    ("system", "You are a legal assistant answering based on documents."),
    ("human", "Context: {context}\n\nQuestion: {query}")
]).format_messages(
    context="Section 420 of IPC explains cheating and dishonesty.",
    query="What is Section 420?"
)
```

📚 **Use Case**: RAG pipeline, context-based QA.

---

## ✅ Summary Table

| Example                 | Input Variables Used         | Use Case                       |
| ----------------------- | ---------------------------- | ------------------------------ |
| Translation Prompt      | `{language}`, `{sentence}`   | Language tools                 |
| Email Generator         | `{client_name}`, `{subject}` | Automation, CRM                |
| Chat Prompt - Support   | `{question}`, `{answer}`     | Customer service bots          |
| Few-Shot Chat Prompt    | `{new_question}`             | Education, tutors              |
| RAG + Context Injection | `{context}`, `{query}`       | Retrieval-Augmented Generation |

---

Next up is:

📘 **4.4 – Few-shot Prompting**
→ Starting with **4.4.1 – What is Few-shot Prompting?**

Would you like to proceed?
