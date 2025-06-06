from langchain_community.chat_models import ChatOllama
from langchain_core.messages import HumanMessage

prompt = [HumanMessage(content=" I want to learn about python print(). Can you teach me in detail?")]

# Deterministic response
llm_0 = ChatOllama(model="llama3", temperature=0.0,base_url= "http://20.244.34.219:11434")
print("0.0 Temp:\n", llm_0.invoke(prompt).content)

# Creative response
llm_1 = ChatOllama(model="llama3", temperature=1.0,base_url="http://20.244.34.219:11434")
print("\n\n\n\n1.0 Temp:\n", llm_1.invoke(prompt).content)
