from pydantic import BaseModel

class SecurityReport(BaseModel):
    domain: str
    owner: str
    risk_level: str
    ip_reputation: str
    recommendation: str
