import whois
from langchain.tools import tool

@tool
def whois_lookup(domain: str) -> str:
    """
    Use this tool when you need ownership,
    registration, expiration, or registrar
    information about a domain.
    """

    try:
        info = whois.whois(domain)

        return f"""
        Domain Name: {domain}
        Registrar: {info.registrar}
        Creation Date: {info.creation_date}
        Expiration Date: {info.expiration_date}
        Organization: {info.org}

        """
    except Exception as e:
        return f"WHOIS lookup failed: {str(e)}"