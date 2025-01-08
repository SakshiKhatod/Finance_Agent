from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
from dotenv import load_dotenv

load_dotenv()
web_agent = Agent(
    name="Web Agent",
    role="Search the web for proper information",
    model=Groq(id="llama3-groq-70b-8192-tool-use-preview"),
    tools=[DuckDuckGo()],
    instructions=["Always include sources"],
    show_tool_calls=True,
    markdown=True,
)

# web_agent.print_response(" share the latest news for NVDA",stream=True)

finance_agent = Agent(
    name="Finance Agent",
    model=Groq(id="llama3-groq-70b-8192-tool-use-preview"),
    tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, company_info=True, company_news=True)],
    instructions=["Use tables to display data"],
    show_tool_calls=True,
    markdown=True,
)
# finance_agent.print_response("Summarize analyst recommendations for NVDA", stream=True)

multi_ai_agent=Agent(
    team=[web_agent,finance_agent],
    model=Groq(id="llama3-groq-70b-8192-tool-use-preview"),
    instructions=["Always include sources","Use tables to display data"],
    show_tool_calls=True,
    markdown=True,
)

multi_ai_agent.print_response("Summarize analyst recommendation and share the latest news for NVDA",stream=True)
