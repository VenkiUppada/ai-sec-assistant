from pydantic import BaseModel

class SecurityReport(BaseModel):
    domain: str | None
    owner: str | None

    ip_address: str | None
    ip_reputation: str | None
    risk_level: str | None

    cve_id: str | None
    severity: str | None
    cvss_score: float | None
    affected_software: str | None

    recommendation: str
