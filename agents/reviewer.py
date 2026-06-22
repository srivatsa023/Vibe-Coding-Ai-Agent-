from utils.llm import ask_llm

def reviewer(report):
    """
    Reviews and improves the final report.
    """

    prompt = f"""
    Review the following startup report.

    Improve:
    - Clarity
    - Professionalism
    - Business feasibility

    Report:
    {report}
    """




    prompt = f"""
    You are a startup consultant.

    Review the startup report below.

    Give:
    1. Strengths
    2. Weaknesses
    3. Suggestions for improvement

    Do NOT rewrite the report.
    Do NOT remove any sections.

    Startup Report:
    {report}
    """

    return ask_llm(prompt)