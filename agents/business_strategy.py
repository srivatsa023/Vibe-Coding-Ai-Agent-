from utils.llm import ask_llm

def business_strategy(research_data):

    prompt = f"""
    Based on this market research:

    {research_data}

    Create:
    1. Revenue Model
    2. Pricing Strategy
    3. Launch Plan
    4. Growth Strategy
    """

    return ask_llm(prompt)