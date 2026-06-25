from agents.swot import swot_analysis
from agents.investor_pitch import investor_pitch
from agents.market_research import market_research
from agents.business_strategy import business_strategy
from agents.website_content import website_content
from agents.marketing import marketing
from agents.reviewer import reviewer

from utils.pdf_export import generate_pdf

import time

# Start timer
start_time = time.time()

# Banner
print("=" * 60)
print("🚀 LaunchPilot AI")
print("Multi-Agent Startup Generator")
print("=" * 60)

# User Input Validation
while True:
    idea = input("\nEnter Startup Idea: ").strip()

    if idea:
        break

    print("❌ Please enter a startup idea.")

# Run Agents
print("\n🔍 Running Market Research Agent...")
research = market_research(idea)
print("✅ Research Complete")

print("\n📊 Running SWOT Agent...")
swot = swot_analysis(idea)
print("✅ SWOT Complete")

print("\n💰 Running Investor Pitch Agent...")
pitch = investor_pitch(idea)
print("✅ Investor Pitch Complete")

print("\n📈 Running Business Strategy Agent...")
strategy = business_strategy(idea, research)
print("✅ Strategy Complete")

print("\n🌐 Running Website Content Agent...")
website = website_content(strategy)
print("✅ Website Content Complete")

print("\n📢 Running Marketing Agent...")
marketing_output = marketing(website)
print("✅ Marketing Complete")

# Combine Outputs
final_report = f"""
MARKET RESEARCH

{research}

============================================================
SWOT ANALYSIS
=============

{swot}

============================================================
INVESTOR PITCH
==============

{pitch}

============================================================
BUSINESS STRATEGY
=================

{strategy}

============================================================
WEBSITE CONTENT
===============

{website}

============================================================
MARKETING
=========

{marketing_output}
"""

# Reviewer Agent
print("\n📝 Running Reviewer Agent...")
reviewed_report = reviewer(final_report)
print("✅ Review Complete")

# Final Combined Report
complete_report = f"""
{final_report}

============================================================
REVIEWER FEEDBACK
=================

{reviewed_report}
"""

# End Timer
end_time = time.time()

# Display Output
print("\n" + "=" * 60)
print("🎉 STARTUP LAUNCH PACK GENERATED")
print("=" * 60)

print(complete_report)

print("\n" + "=" * 60)
print(f"⏱️ Total Processing Time: {end_time - start_time:.2f} seconds")
print("=" * 60)

# Save TXT Report
with open("startup_report.txt", "w", encoding="utf-8") as file:
    file.write(complete_report)

print("\n📄 Report saved as startup_report.txt")

# Save PDF Report
generate_pdf(complete_report)

print("📄 PDF saved as startup_report.pdf")

