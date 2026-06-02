import requests
from langchain.tools import tool
from utils.logger import logger

@tool
def cve_lookup(cve_id: str) -> str:
    """
    Use this tool when the user asks about
    CVEs, vulnerabilities, exploits,
    severity ratings, affected software,
    or security advisories.
    """
    logger.info(f"Running CVE lookup for {cve_id}")

    try:

        url = (
            f"https://services.nvd.nist.gov/rest/json/cves/2.0?cveId={cve_id}"
        ) 

        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
        print(data.keys())

        vulnerability = data.get(
            "vulnerabilities", []
        ) 

        if not vulnerability: 
            return "CVE not found or no details available."
        
        cve = vulnerability[0]["cve"]

        description = cve["descriptions"][0]["value"]
        matries = cve.get("metrics", {})
        severity = "Unknown"
        score = "Unknown"

        if "cvssMetricV31" in matries:
            matric = matries["cvssMetricV31"][0]
            severity = matric["cvssData"]["baseSeverity"]
            score = matric["cvssData"]["baseScore"]
        return f"""
        CVE ID: {cve_id}
        Severity: {severity}
        CVSS Score: {score}
        Description: {description}
        """
    except Exception as e:

        logger.error(f"CVE lookup failed: {str(e)}")
        return f"CVE lookup failed: {str(e)}"