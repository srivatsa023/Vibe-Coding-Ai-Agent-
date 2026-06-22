from utils.llm import ask_llm

def swot_analysis(startup_idea):
    prompt = f"""
    Perform a SWOT Analysis for this startup idea:

    Startup Idea:
    {startup_idea}

    Provide:

    Strengths
    Weaknesses
    Opportunities
    Threats

    Make it professional and detailed.
    """

    return ask_llm(prompt)
