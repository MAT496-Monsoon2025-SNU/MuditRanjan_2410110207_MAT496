from langchain_mcp_adapters.client import MultiServerMCPClient
from langgraph.prebuilt import create_react_agent

client = MultiServerMCPClient(
    {
        "math": {
            "command": "python",
            # Make sure to update to the full absolute path to your math_server.py file
            "args": [r"C:\\Users\\dell\\Documents\\CODES\\MAT496\\MCP\\servers\\math_server.py"],
            "transport": "stdio",
        },
    }
)
tools = await client.get_tools()
agent = create_react_agent("groq:openai/gpt-oss-120b", tools)
math_response = await agent.ainvoke({"messages": "what's (3 + 5) x 12?"})
weather_response = await agent.ainvoke({"messages": "what is the weather in nyc?"})