from langchain.agents import create_agent

from models.llm_factory import get_gemini
import tools.whois_tool as whois_tool
import tools.ip_reputation_tool as ip_reputation_tool

llm = get_gemini()

agent = create_agent(
    model=llm,
    tools=[whois_tool.whois_lookup, ip_reputation_tool.ip_reputation_lookup]

)