from langchain.tools import tool

@tool
def ip_reputation_lookup(ip_address: str)-> str:
    """
    Use this tool when the user asks about IP reputaion, malicious IPs, suspicious IP Addresses, abuse reports, or threat intelligence realated to an IP address.
    """

    mock_data = {
        "8.8.8.8": "Low Risk. Google Public DNS. No malicious reports.",
        "1.1.1.1": "Low Risk. Cloudflare DNS. No malicious reports.",
        "123.123.123.123": "High Risk. Multiple abuse reports detected."
    }

    return mock_data.get(
        ip_address,
        "Unknown IP. No reputation data available."
    )