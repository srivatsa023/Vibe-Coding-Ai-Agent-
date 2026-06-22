from utils.llm import ask_llm

def website_content(strategy):

    prompt = f"""
    Based on this startup strategy:

    {strategy}

    Generate:
    1. Homepage Headline
    2. Subheadline
    3. About Us
    4. Features
    5. CTA
    6. FAQ
    """

    return ask_llm(prompt)