Perfect! Let’s move to:

---

## 📘 4.3.2 – Syntax and Formatting Rules for Input Variables

---

### 🎯 Goal:

Learn the **rules, formatting options, and common patterns** when working with input variables in `PromptTemplate` and `ChatPromptTemplate`.

---

## 🔤 1. Basic Syntax

Input variables are **wrapped in curly braces** like:

```python
{variable_name}
```

These are replaced by values passed via `.format()` or in a chain.

---

### ✅ Example – PromptTemplate

```python
from langchain.prompts import PromptTemplate

template = PromptTemplate.from_template(
    "Hello {name}, today is {day}."
)

formatted = template.format(name="Alice", day="Wednesday")
print(formatted)
```

🟢 Output:

```
Hello Alice, today is Wednesday.
```

---

## 🧠 2. Multiple Input Variables

You can include **as many variables** as needed:

```python
PromptTemplate.from_template(
    "You are {role}. Your task is to {task} on {date}."
)
```

Then format it with:

```python
.format(role="manager", task="submit reports", date="Friday")
```

---

## 📋 3. Reusing Variables in the Same Template

You can **reuse the same variable** in multiple places:

```python
template = PromptTemplate.from_template(
    "Hello {name}. Yes, I said {name}!"
)
```

✅ Output:

```
Hello Bob. Yes, I said Bob!
```

---

## ❌ 4. Invalid Formatting Examples (and Fixes)

| ❌ Problem                | 💡 Fix                                                |
| ------------------------ | ----------------------------------------------------- |
| Missing variable         | Ensure all `{}` placeholders have corresponding input |
| Extra variable passed    | Only pass inputs that exist in the template           |
| Typo in placeholder name | Double-check names used in `.format()` and template   |

---

### Example of Error

```python
template = PromptTemplate.from_template("Hi {name}")
template.format(person="Bob")  # ❌ KeyError
```

Fix:

```python
template.format(name="Bob")    # ✅
```

---

## 🧱 5. ChatPromptTemplate Formatting

Each message can have its own variables:

```python
ChatPromptTemplate.from_messages([
    ("system", "You are a {profession}."),
    ("human", "Tell me more about {topic}.")
]).format_messages(profession="doctor", topic="cardiology")
```

✅ Output:

```
SystemMessage(content="You are a doctor.")
HumanMessage(content="Tell me more about cardiology.")
```

---

## 🔁 6. Advanced: Formatting Lists and Loops

If you want to include a **list** or multiple values:

```python
PromptTemplate.from_template(
    "Your tasks:\n{task_list}"
).format(task_list="\n".join(["1. Write code", "2. Fix bugs"]))
```

---

## ✅ Summary Table

| Rule                            | Description                                         |
| ------------------------------- | --------------------------------------------------- |
| `{variable}`                    | Basic syntax                                        |
| `.format(var1=val1, var2=val2)` | Call to inject values                               |
| Auto-detection                  | Variables auto-inferred from curly braces           |
| Message-specific placeholders   | Each message can use unique variables in ChatPrompt |
| List formatting                 | Use `.join()` or string formatting manually         |
| Error-prone scenarios           | Missing or extra inputs                             |

---

Would you like to continue to:

📘 **4.3.3 – Real-World Examples Using Input Variables**?
