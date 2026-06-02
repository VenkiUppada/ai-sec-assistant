from langchain_core.messages import ToolMessage
from utils.logger import logger
from agents.security_agent import agent
from agents.report_generator import generate_report


def investigate(query: str):
    logger.info(f"Starting investigation for query: {query}")
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

    logger.info("Agent execution completed ")

    tool_output = []

    for msg in response["messages"]:

        if isinstance(msg, ToolMessage):

            logger.info(f"Collected output from tool: {msg.name}")

            tool_output.append(
                f"""
            Tool: {msg.name}

            Output:
            {msg.content}
            """
            )
    
    findings = "\n\n".join(tool_output)
    logger.info("Generating structured report from findings")
    report = generate_report(findings)
    logger.info("Report generated successfully")
    return report