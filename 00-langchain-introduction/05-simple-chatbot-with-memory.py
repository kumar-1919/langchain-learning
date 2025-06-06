from langchain.memory import ConversationBufferMemory
from langchain_community.llms import Ollama
from langchain.chains import LLMChain
from langchain_core.prompts import ChatPromptTemplate

# 1. Load LLM
llm = Ollama(model="llama3")

# 2. Setup memory
memory = ConversationBufferMemory(return_messages=True)

# 3. Define prompt
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful AI assistant."),
    ("human", "{input}"),
])

# 4. Create LLM chain with memory
chatbot_chain = LLMChain(
    llm=llm,
    prompt=prompt,
    memory=memory,
    verbose=True
)

# 5. Simulate chat
print(chatbot_chain.run("Hi, I'm John."))
print(chatbot_chain.run("Can you remind me what I just said?"))
