Perfect! Let’s continue with:

---

## 📘 4.4.2 – Implementing Few-shot Prompting using `FewShotPromptTemplate`

---

### 🎯 Goal:

Learn how to use LangChain’s built-in `FewShotPromptTemplate` to create reusable, dynamic few-shot prompts more efficiently.

---

## 🧱 What is `FewShotPromptTemplate`?

LangChain provides `FewShotPromptTemplate` to:

* Automate few-shot formatting
* Separate **examples** from **main prompt**
* Improve **reusability** and **clean code**

---

## 🧰 When to Use It?

Use `FewShotPromptTemplate` when:

✅ You want to reuse the same examples across multiple inputs
✅ You want to separate logic (examples) from prompt structure
✅ You want to dynamically load or switch examples

---

## 🔧 Syntax & Constructor

```python
FewShotPromptTemplate(
    examples: List[Dict[str, str]],       # Your input-output examples
    example_prompt: PromptTemplate,       # How to format each example
    prefix: str = "",                     # Text before the examples
    suffix: str = "",                     # Text after the examples
    input_variables: List[str]            # Final prompt variables
)
```

✅ Default behavior:

* Merges all examples
* Adds prefix and suffix
* Applies `.format()` with user input

---

## 🧪 Example – Sentiment Classifier

### ➤ Step 1: Define `example_prompt`

```python
from langchain.prompts import PromptTemplate, FewShotPromptTemplate

example_prompt = PromptTemplate.from_template(
    "Input: {text}\nOutput: {label}"
)
```

---

### ➤ Step 2: Define `examples`

```python
examples = [
    {"text": "I love this!", "label": "Positive"},
    {"text": "This is awful.", "label": "Negative"}
]
```

---

### ➤ Step 3: Combine into `FewShotPromptTemplate`

```python
prompt = FewShotPromptTemplate(
    examples=examples,
    example_prompt=example_prompt,
    prefix="Classify the sentiment below:\n",
    suffix="Input: {user_text}\nOutput:",
    input_variables=["user_text"]
)
```

---

### ➤ Step 4: Format Prompt

```python
final_prompt = prompt.format(user_text="I really like the UI design.")
print(final_prompt)
```

🟢 Output:

```
Classify the sentiment below:

Input: I love this!
Output: Positive
Input: This is awful.
Output: Negative
Input: I really like the UI design.
Output:
```

---

## 🧠 Dynamic Example Loading

You can **dynamically pull examples** from a database, CSV, or file and plug them in.

```python
def load_examples():
    return [
        {"text": "Great app", "label": "Positive"},
        {"text": "Terrible update", "label": "Negative"},
    ]

prompt = FewShotPromptTemplate(
    examples=load_examples(),
    ...
)
```

---

## 📘 Summary Table

| Parameter         | Description                                       |
| ----------------- | ------------------------------------------------- |
| `examples`        | List of example dicts with variable → value       |
| `example_prompt`  | How each example is formatted                     |
| `prefix`          | Text before examples (optional)                   |
| `suffix`          | Final instruction with input variable             |
| `input_variables` | Variables used in the suffix                      |
| Use case          | Classification, translation, formatting, QA, etc. |

---

### 🔖 Bonus Tip:

You can also use `ChatPromptTemplate` with few-shot examples by chaining message templates, but for most static examples, `FewShotPromptTemplate` is more readable and maintainable.

---

Would you like to continue to:

📘 **4.5 – Chains**
→ Starting with **4.5.1 – What is a Chain in LangChain?**
