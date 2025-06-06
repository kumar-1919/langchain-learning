Great! Let's continue with:

---

## 📘 3.4 – **Synchronous vs Asynchronous Calls in LangChain**

---

### 🎯 Goal:

Understand the difference between **sync** and **async** calls in LangChain, how they affect performance, how to use them properly, and when to prefer one over the other.

---

### 📘 Curriculum for 3.4

| Topic                    | Description                                     |
| ------------------------ | ----------------------------------------------- |
| ✅ What is Sync vs Async? | Basic explanation with Python context           |
| ⚙️ Function Syntax       | `invoke()` vs `ainvoke()`                       |
| 🧠 Technical Terms       | Coroutine, Event Loop, Blocking vs Non-blocking |
| 📅 When to Use Which     | Use cases: sequential vs parallel calls         |
| 🧪 Code Examples         | Both `invoke()` and `ainvoke()` usage           |
| ⚡ Performance Benefit    | Async = speed via concurrency                   |
| 📄 Summary Table         | Comparison table with pros/cons                 |

---

## ✅ What Is Synchronous vs Asynchronous?

| Type             | Explanation                                                        |
| ---------------- | ------------------------------------------------------------------ |
| **Synchronous**  | Code executes one line at a time, waits for each result (blocking) |
| **Asynchronous** | Code *starts* a task, *doesn't wait*, and continues (non-blocking) |

---

## ⚙️ Function Syntax in LangChain

All LangChain models (LLMs, Chains, Tools) support:

| Type  | Function    | Description                            |
| ----- | ----------- | -------------------------------------- |
| Sync  | `invoke()`  | Blocking call; waits for result        |
| Async | `ainvoke()` | Non-blocking call; returns a coroutine |

---

### ⚠️ Note:

To use `ainvoke()`:

* You must be inside an `async` function.
* Python version ≥ 3.7 recommended.
* You need to use `await`.

---

## 🧪 Code Examples

---

### ✅ Synchronous Example (`invoke()`)

```python
from langchain_community.chat_models import ChatOllama
from langchain_core.messages import HumanMessage

llm = ChatOllama(model="llama3")

result = llm.invoke([HumanMessage(content="What is the capital of Japan?")])
print(result.content)
```

---

### ✅ Asynchronous Example (`ainvoke()`)

```python
import asyncio
from langchain_community.chat_models import ChatOllama
from langchain_core.messages import HumanMessage

async def main():
    llm = ChatOllama(model="llama3")
    result = await llm.ainvoke([HumanMessage(content="Explain relativity")])
    print(result.content)

asyncio.run(main())
```

---

## 🧠 Technical Terms

| Term             | Meaning                                                    |
| ---------------- | ---------------------------------------------------------- |
| **Coroutine**    | A function declared with `async def`, which can be awaited |
| **Event Loop**   | Manages and schedules execution of async tasks             |
| **Blocking**     | Waits until a task is done                                 |
| **Non-blocking** | Starts task and keeps going; result comes later            |

---

## 📅 When to Use Which?

| Scenario                        | Use                            |
| ------------------------------- | ------------------------------ |
| Single step LLM calls           | `invoke()`                     |
| Multiple parallel LLM calls     | `ainvoke()` (async)            |
| Chains that require speed-up    | `ainvoke()` inside `async def` |
| Streamlit or simple CLI tools   | `invoke()`                     |
| Web apps (e.g., FastAPI, Flask) | Prefer async (`ainvoke()`)     |

---

## ⚡ Performance Tip

Running multiple LLMs or tools in **parallel** using `async` can reduce total time:

```python
# Async parallel call example
async def get_responses():
    task1 = llm.ainvoke([HumanMessage(content="Joke about elephants")])
    task2 = llm.ainvoke([HumanMessage(content="Joke about monkeys")])
    results = await asyncio.gather(task1, task2)
    return results
```

---

## 📄 Summary Table

| Feature      | Synchronous               | Asynchronous                        |
| ------------ | ------------------------- | ----------------------------------- |
| Function     | `invoke()`                | `ainvoke()`                         |
| Execution    | One by one (blocking)     | Multiple in parallel (non-blocking) |
| Suitable For | Simple apps, scripts      | High-performance apps               |
| Requirements | None                      | Must use `async def` + `await`      |
| Performance  | Slower for multiple calls | Much faster for many tasks          |

---

✅ That’s everything you need to know about **Synchronous vs Asynchronous LLM calls** in LangChain.

Shall we move on to the next main topic:
📘 **Section 4 – Prompt Templates**?

Would you like the curriculum for that first?
