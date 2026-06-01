from models.llm_factory import get_gemini, get_groq
import tools.whois_tool as whois_tool
def main():
    # gemini = get_gemini()
    # groq = get_groq()

    # # response_gemini = gemini.invoke()
    # # response_groq = groq.invoke()

    # for chunk in gemini.stream("what is SQl injection? Explane with real worlkd examples"):
    #     print(chunk.content, end=" ", flush=True)
    #     print("\n")
    # for chunk in groq.stream("what is XSS? Explane with real world examples"):
    #     print(chunk.content, end=" ", flush=True)
    #     print("\n")


    result = whois_tool.whois_lookup.invoke(
        {"domain": "google.com"}
    )

    print(result)
    print(whois_tool.whois_lookup.name)
    print(whois_tool.whois_lookup.description)

if __name__ == "__main__":
    main()
