import tools.cve_tool as cve_tool
import agents.security_agent as security_agent

response = security_agent.agent.invoke(
    {
        "messages": [
            {
                "role": "user",
                "content": "Tell me about CVE-2021-44228"
            }
        ]
    }
)
print(response)