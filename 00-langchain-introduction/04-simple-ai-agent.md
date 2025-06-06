Great! Let's start with:

---

## 🤖 **1.2.2 Agents**

---

### ✅ What is an Agent in LangChain?

An **Agent** is an **LLM-powered decision-maker** that can:

* Decide **what action to take next**
* Choose from a set of **available tools**
* Use those tools **in a loop** until it reaches the final answer

> 🧠 Think of an Agent as a smart assistant that can **reason**, **plan**, and **act** — not just answer questions, but solve problems step-by-step by using tools like calculators, search engines, code interpreters, or APIs.

---

### 🔍 Why do we need Agents?

Static chains (like `LLMChain`) follow **fixed logic**:

> input → prompt → LLM → output

But real-world tasks often need:

* **Tool selection** (e.g., “Should I Google this or calculate it?”)
* **Multiple steps** (e.g., “Search → Fetch → Analyze → Answer”)
* **Dynamic decisions** (e.g., retrying a failed API call)

Agents add this **flexibility**, making LLMs more like human assistants.

---

### 📅 When to use Agents?

Use Agents when your app:

* Requires **multiple tools** (search, API, calculator, Python, etc.)
* Needs **multi-step reasoning**
* Can't be solved using a single fixed prompt or chain

Examples:

* AI Assistant that can **search, summarize, and schedule** meetings
* Customer support bot that can **query database, apply logic, and respond**
* Developer copilot that can **analyze code + generate + run snippets**

---

### 🌍 Where are Agents used?

| Domain           | Agent Use Case Example                                                      |
| ---------------- | --------------------------------------------------------------------------- |
| Customer Support | Tool-using chatbot that checks order status and explains refund policy      |
| Healthcare       | Agent that pulls patient history, applies rules, and recommends actions     |
| Finance          | Agent that fetches data, runs calculations, and makes portfolio suggestions |
| Education        | AI tutor that searches Wikipedia + solves math with calculator              |

---

### ⚙️ Key Components of LangChain Agents

| Component         | Description                                                   |
| ----------------- | ------------------------------------------------------------- |
| **AgentExecutor** | Executes the logic loop (decide, act, observe, repeat)        |
| **Tool**          | A function the agent can call (e.g., Search, Calculator, API) |
| **Toolkits**      | Predefined sets of tools for domains (e.g., SQL, bash, web)   |
| **LLM**           | The brain behind decisions (e.g., GPT-4, LLaMA)               |
| **Prompt**        | System message to guide agent behavior                        |
| **OutputParser**  | Parses tool outputs to feed back into the loop                |

---

### 🧪 Minimal Code Example (LangChain v0.1+ — latest version)

Let’s build an agent that uses **math + search** tools:

```python
from langchain_community.llms import Ollama
from langchain.agents import Tool, initialize_agent
from langchain.agents.agent_types import AgentType
from langchain.tools import DuckDuckGoSearchRun
from langchain.tools.python.tool import PythonREPLTool

# 1. Load LLM
llm = Ollama(model="llama3")

# 2. Define tools
search_tool = DuckDuckGoSearchRun()
calculator_tool = PythonREPLTool()

tools = [
    Tool(name="Search", func=search_tool.run, description="Search the web for recent facts"),
    Tool(name="Calculator", func=calculator_tool.run, description="Do math operations"),
]

# 3. Initialize agent
agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)

# 4. Run agent
response = agent.run("What is the square root of the population of India?")
print(response)
```

✅ This uses modern agent setup with `initialize_agent()` and supports multiple tools.

---

### 🧠 Technical Terms

| Term              | Meaning                                                          |
| ----------------- | ---------------------------------------------------------------- |
| **Agent**         | LLM-based reasoner and actor                                     |
| **Tool**          | A callable utility like search, calculator, or database function |
| **AgentExecutor** | The loop engine that runs the agent's thought-action cycles      |
| **Toolkits**      | Groups of tools (e.g., WebToolKit, SQLToolKit)                   |
| **Prompt**        | Special system prompt that defines how the agent behaves         |

---

### 📄 Summary Table

| Field          | Description                                                         |
| -------------- | ------------------------------------------------------------------- |
| What           | LLM-powered decision-maker that uses tools and reasons step-by-step |
| Why            | For dynamic, multi-step, tool-using tasks                           |
| When to use    | When a single prompt/chain is not enough                            |
| Where to use   | Complex apps (AI assistants, research agents, planners, etc.)       |
| Key Components | AgentExecutor, Tools, Toolkits, Prompts, LLMs                       |

---

Would you like to continue with **1.2.3 Chatbots** next?
