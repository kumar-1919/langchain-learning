from langchain_community.llms import Ollama
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableSequence

llm = Ollama(model="llama3")

prompt = PromptTemplate.from_template("Summarize: {text}")

pipeline = RunnableSequence(steps=[prompt, llm])

result = pipeline.invoke({"text": "LangChain is a framework for composing LLM applications."})
print(result)
