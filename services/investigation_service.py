from langchain_core.messages import ToolMessage

from agents.security_agent import agent
from agents.report_generator import generate_report

def investigate(query: str):

    response = agent.invoke(
        {
            "messages": [
                {
                    "role": "user",
                    "content": query
                }
            ]
        }
    )

    tool_output = []

    for msg in response["messages"]:

        if isinstance(msg, ToolMessage):
            tool_output.append(msg.content)
    
    findings = "\n\n".join(tool_output)
    report = generate_report(findings)
    return report