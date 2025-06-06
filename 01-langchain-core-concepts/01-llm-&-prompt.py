from langchain_community.llms import Ollama
from langchain_core.prompts import PromptTemplate

# 1. Load LLM
llm = Ollama(model="llama3", temperature=0.3)

# 2. Create prompt template
prompt = PromptTemplate.from_template("Write a short poem about {topic}")

# 3. Format input and run LLM
formatted_prompt = prompt.format(topic="the moon")
response = llm.invoke(formatted_prompt)

print(response)
