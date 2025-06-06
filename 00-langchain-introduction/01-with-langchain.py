from langchain_openai import ChatOpenAI

llm = ChatOpenAI(
    model="gpt-4",
    openai_api_key="your-api-key"  # Or use environment variable instead
)

response = llm.invoke("What is LangChain?")
print(response)

"""
from langchain_openai import ChatOpenAI
from langchain.schema import HumanMessage

llm = ChatOpenAI(model="gpt-4")
response = llm([HumanMessage(content="What's the capital of France?")])
print(response.content)
"""