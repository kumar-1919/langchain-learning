Perfect! Let’s now move to:

---

## 📘 4.1.2 – Syntax and Usage of `PromptTemplate`

---

### 🎯 Goal:

Understand the **class structure**, **methods**, and **usage patterns** of `PromptTemplate`, along with syntax, parameters, and supported methods — all aligned with production-level best practices.

---

## 🧱 `PromptTemplate` – Class Syntax

```python
PromptTemplate(
    input_variables: List[str],
    template: str,
    validate_template: bool = True,
    template_format: str = "f-string"
)
```

---

### 📌 Parameter Details

| Parameter           | Type        | Required | Default      | Description                                                                  |
| ------------------- | ----------- | -------- | ------------ | ---------------------------------------------------------------------------- |
| `input_variables`   | `List[str]` | ✅ Yes    | —            | List of variable names used in the template                                  |
| `template`          | `str`       | ✅ Yes    | —            | The template string containing `{}` placeholders                             |
| `validate_template` | `bool`      | ❌ No     | `True`       | If `True`, validates that all placeholders are declared in `input_variables` |
| `template_format`   | `str`       | ❌ No     | `"f-string"` | Type of formatting; `"f-string"` or `"jinja2"`                               |

---

### 🧠 Common Methods

| Method               | Description                                                  |
| -------------------- | ------------------------------------------------------------ |
| `.format(**kwargs)`  | Replace placeholders with actual values                      |
| `.format_prompt()`   | Returns a `PromptValue` object for use with chains           |
| `.partial(**kwargs)` | Pre-fill some input variables, returning a new prompt object |

---

## 🧪 Usage Examples

---

### ✅ Basic Usage

```python
from langchain.prompts import PromptTemplate

template = PromptTemplate(
    input_variables=["topic"],
    template="Write a short story about {topic}."
)

print(template.format(topic="space exploration"))
```

🟢 **Output:**

```
Write a short story about space exploration.
```

---

### ✅ Using `.format_prompt()` with Chains

```python
prompt = PromptTemplate(
    input_variables=["name"],
    template="Greet {name} with a fun fact about whales."
)

formatted_prompt = prompt.format_prompt(name="Sam")
print(formatted_prompt.to_string())
```

🟢 Output:

```
Greet Sam with a fun fact about whales.
```

* `format_prompt()` is often used when chaining with LLMs or RunnableSequence.

---

### ✅ Using `.partial()` to pre-fill variables

```python
prompt = PromptTemplate(
    input_variables=["animal", "emotion"],
    template="Describe a {animal} that looks very {emotion}."
)

# Pre-filling the animal
partial_prompt = prompt.partial(animal="dolphin")
print(partial_prompt.format(emotion="happy"))
```

🟢 Output:

```
Describe a dolphin that looks very happy.
```

---

## 🔧 Optional Template Format: `jinja2`

```python
PromptTemplate(
    input_variables=["place"],
    template="Welcome to {{ place }}!",
    template_format="jinja2"
)
```

> Use this if you want `{{ }}` style templates instead of `{ }`.

---

## ⚠️ Common Errors and Solutions

| Error Message                        | Reason                                      | Fix                                 |
| ------------------------------------ | ------------------------------------------- | ----------------------------------- |
| `ValueError: Missing input variable` | Placeholder not listed in `input_variables` | Add it to `input_variables`         |
| `KeyError: variable not found`       | Called `.format()` without required key     | Pass all variables in `.format()`   |
| `Unsupported template_format`        | Invalid template type                       | Use `"f-string"` or `"jinja2"` only |

---

## ✅ Summary Table

| Feature              | Value                                         |
| -------------------- | --------------------------------------------- |
| Class                | `PromptTemplate`                              |
| Required Params      | `input_variables`, `template`                 |
| Optional Params      | `validate_template`, `template_format`        |
| Default Format Style | `"f-string"`                                  |
| Useful Methods       | `.format()`, `.format_prompt()`, `.partial()` |
| Compatible With      | Chains, LLMs, RunnableSequence                |
| Errors to Handle     | Missing variables, format mismatch            |

---

Would you like to proceed to the next sub-subtopic?
📘 **4.1.3 – Use Cases of `PromptTemplate`**?