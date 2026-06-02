from models.llm_factory import get_gemini, get_groq
from schemas.security_report import SecurityReport

llm = get_groq()

structured_llm = llm.with_structured_output(SecurityReport)

def generate_report(findings: str) -> SecurityReport:
    """
    Convert investigation findings into a structured security report.
    """
    return structured_llm.invoke(findings)

