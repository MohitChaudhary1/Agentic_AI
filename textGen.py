from smolagents import CodeAgent, DuckDuckGoSearchTool, HfApiModel
from dotenv import load_dotenv

load_dotenv()

# Initialize agent with only supported parameters
agent = CodeAgent(
    tools=[DuckDuckGoSearchTool()],
    model=HfApiModel(),
    additional_authorized_imports=["requests", "markdownify"]
)

# Run the agent
result = agent.run("What is Mahatma Gandhi's preferred pet?")
print(result)