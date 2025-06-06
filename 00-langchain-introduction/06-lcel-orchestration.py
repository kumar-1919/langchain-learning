from langchain_community.llms import Ollama
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableSequence

# 1. Load LLM
llm = Ollama(model="llama3")

# 2. Create Prompt
prompt = PromptTemplate.from_template("Translate the following to French: {text}")

# 3. Compose Runnable Chain (Prompt → LLM → Output)
chain = RunnableSequence(
    steps=[
        prompt,
        llm
    ]
)

# 4. Run chain
result = chain.invoke({"text": "Hello, how are you?"})
print(result)