You're absolutely right — thanks for pointing that out.

For the last topic (📘 **3.4 – Synchronous vs Asynchronous Calls**), I covered the *concepts and examples* but did not fully explain the **syntax of functions/methods/statements** (like `invoke()`, `ainvoke()`, `asyncio.run()`, etc.) as per your specified learning format.

---

Let me quickly **rectify that now** by giving the **function syntax explanations** for everything used in that topic:

---

## ✅ Syntax Deep Dive – From 3.4: Sync vs Async Calls

---

### 1️⃣ `invoke()`

```python
llm.invoke(input: Union[str, List[BaseMessage]]) -> BaseMessage
```

#### 📌 Parameters:

| Name    | Type                       | Required | Description                      |
| ------- | -------------------------- | -------- | -------------------------------- |
| `input` | `str` or list of `Message` | ✅ Yes    | The prompt or message(s) to send |

#### ✅ Default Behavior:

* It is **blocking** – it waits until the result is returned.

#### ✅ Example:

```python
result = llm.invoke("Tell me a joke")
print(result.content)
```

---

### 2️⃣ `ainvoke()`

```python
await llm.ainvoke(input: Union[str, List[BaseMessage]]) -> BaseMessage
```

#### 📌 Parameters:

Same as `invoke()`, but:

* You **must call** it inside an `async def` function.
* You **must use `await`** keyword.

#### ✅ Example:

```python
async def main():
    result = await llm.ainvoke("Hello")
    print(result.content)
```

---

### 3️⃣ `async def`

```python
async def function_name():
    # async code
```

* Declares a **coroutine**.
* Needed to use `await`.

---

### 4️⃣ `await`

* Pauses the current coroutine until the awaited coroutine is done.

```python
await llm.ainvoke("Explain gravity")
```

---

### 5️⃣ `asyncio.run()`

```python
asyncio.run(coro: Coroutine)
```

* Runs an async function **at the top-level** (like in a script or notebook).

#### ✅ Example:

```python
asyncio.run(main())
```

This starts the event loop and runs the `main()` async function.

---

## ✅ Recap Table – Syntax Summary

| Function        | Syntax / Signature         | Notes                                 |                           |
| --------------- | -------------------------- | ------------------------------------- | ------------------------- |
| `invoke()`      | \`llm.invoke(input: str    | List\[Message])\`                     | Sync; blocks until result |
| `ainvoke()`     | `await llm.ainvoke(input)` | Async; requires `async def` + `await` |                           |
| `async def`     | `async def myfunc():`      | Defines a coroutine                   |                           |
| `await`         | `await some_async_func()`  | Waits for the coroutine to finish     |                           |
| `asyncio.run()` | `asyncio.run(myfunc())`    | Runs async code in script / notebook  |                           |

---

Thanks again for catching that! I’ll make sure all future responses — including the **next topic 4.1.1 – PromptTemplate** — will follow **every part of your learning specification**, especially:

* 🔍 Explaining syntax
* ⚙️ Covering function/method parameters
* ✅ Default, required, min/max values
* 🧪 Code + output
* 📄 Summary tables

Shall we now continue with **📘 4.1.1 – What is PromptTemplate?**
