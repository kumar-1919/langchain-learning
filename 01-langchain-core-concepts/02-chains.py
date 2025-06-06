from langchain_community.llms import Ollama
from langchain.chains import LLMChain
from langchain_core.prompts import PromptTemplate

# Load LLM
llm = Ollama(model="llama3")

# Create prompt template
prompt = PromptTemplate.from_template("Explain {topic} in simple words")

# Create a chain
chain = LLMChain(llm=llm, prompt=prompt)

# Run the chain
response = chain.invoke({"topic": "quantum computing"})
print(response)
