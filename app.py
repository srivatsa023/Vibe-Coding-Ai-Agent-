from agents.market_research import market_research
from agents.business_strategy import business_strategy
from agents.website_content import website_content
from agents.marketing import marketing
from agents.reviewer import reviewer

import time

# Start timer
start_time = time.time()

# Banner
print("=" * 60)
print("🚀 LaunchPilot AI")
print("Multi-Agent Startup Generator")
print("=" * 60)

# User Input
# User Input Validation
while True:
    idea = input("\nEnter Startup Idea: ").strip()

    if idea:
        break

    print("❌ Please enter a startup idea.")

print("\n🔍 Running Market Research Agent...")
research = market_research(idea)
print("✅ Research Complete")

print("\n📈 Running Business Strategy Agent...")
strategy = business_strategy(research)
print("✅ Strategy Complete")

print("\n🌐 Running Website Content Agent...")
website = website_content(strategy)
print("✅ Website Content Complete")

print("\n📢 Running Marketing Agent...")
marketing_output = marketing(website)
print("✅ Marketing Complete")

# Combine all outputs
final_report = f"""
==============================
MARKET RESEARCH
==============================

{research}

==============================
BUSINESS STRATEGY
==============================

{strategy}

==============================
WEBSITE CONTENT
==============================

{website}

==============================
MARKETING CONTENT
==============================

{marketing_output}
"""

print("\n📝 Running Reviewer Agent...")
reviewed_report = reviewer(final_report)
print("✅ Review Complete")

# End timer
end_time = time.time()

# Final Output
print("\n" + "=" * 60)
print("🎉 STARTUP LAUNCH PACK GENERATED")
print("=" * 60)

print(reviewed_report)

print("\n" + "=" * 60)
print(f"⏱️ Total Processing Time: {end_time - start_time:.2f} seconds")
print("=" * 60)


with open("startup_report.txt", "w", encoding="utf-8") as file:
    file.write(reviewed_report)

print("\n📄 Report saved as startup_report.txt")