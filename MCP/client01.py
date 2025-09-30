import asyncio
import sys

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
from langchain_mcp_adapters.tools import load_mcp_tools
from langgraph import create_react_agent


async def main():
    server_params = StdioServerParameters(
        command=sys.executable,  # safer than plain "python"
        args=[r"C:\\Users\\dell\\Documents\\CODES\\MAT496\\MCP\\servers\\math_server.py"],
    )

    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            # Initialize the connection
            await session.initialize()

            # Get tools
            tools = await load_mcp_tools(session)

            # Create and run the agent
            agent = create_react_agent("groq:openai/gpt-oss-120b", tools)
            agent_response = await agent.ainvoke({"messages": "what's (3 + 5) x 12? Use the given tools to calculate."})
            print("Agent response:", agent_response)


if __name__ == "__main__":
    asyncio.run(main())