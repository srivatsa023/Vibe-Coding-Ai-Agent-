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

    return ask_llm(prompt)