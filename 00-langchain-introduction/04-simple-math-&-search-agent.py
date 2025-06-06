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
