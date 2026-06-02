from services.investigation_service import investigate

report = investigate(
    "Who owns google.com and is 8.8.8.8 malicious?"
)

print(report)