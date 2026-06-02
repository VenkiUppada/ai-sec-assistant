from langchain.agents import create_agent


from models.llm_factory import get_gemini, get_groq
import tools.whois_tool as whois_tool
import tools.ip_reputation_tool as ip_reputation_tool
import tools.cve_tool as cve_tool


llm = get_groq()

agent = create_agent(
    model=llm,
    tools=[
        whois_tool.whois_lookup, 
        ip_reputation_tool.ip_reputation_lookup,
        cve_tool.cve_lookup
        ]

)