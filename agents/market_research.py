from utils.llm import ask_llm

def market_research(startup_idea):

    prompt = f"""
    Analyze this startup idea:

    {startup_idea}

    Give:
    1. Target Audience
    2. Competitors
    3. Market Opportunities
    4. Risks
    """

    return ask_llm(prompt)