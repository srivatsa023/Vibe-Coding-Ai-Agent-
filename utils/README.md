# 🚀 LaunchPilot AI

LaunchPilot AI is a multi-agent AI system that transforms a startup idea into a complete startup launch package.

Instead of generating a single response, LaunchPilot AI uses multiple specialized AI agents that collaborate to analyze, strategize, create content, generate marketing materials, and review the final output.

---

# Problem Statement

Many aspiring entrepreneurs have great startup ideas but struggle with:

- Conducting market research
- Understanding competitors
- Creating business strategies
- Developing website content
- Creating marketing campaigns
- Reviewing business plans

These tasks often require multiple tools, significant time, and business expertise.

---

# Solution

LaunchPilot AI automates the startup planning process using a chain of AI agents.

A user simply enters a startup idea and the system generates:

- Market Research
- Business Strategy
- Website Content
- Marketing Materials
- Final Reviewed Report

This helps entrepreneurs move from idea to execution much faster.

---

# Features

## 🔍 Market Research Agent

Analyzes:

- Target Audience
- Competitors
- Market Opportunities
- Business Risks

---

## 📈 Business Strategy Agent

Generates:

- Revenue Model
- Pricing Strategy
- Launch Plan
- Growth Strategy

---

## 🌐 Website Content Agent

Creates:

- Homepage Headline
- Subheadline
- About Us Section
- Features Section
- Call To Action
- FAQ

---

## 📢 Marketing Agent

Generates:

- Instagram Posts
- LinkedIn Posts
- Marketing Taglines
- Email Campaigns
- Advertisement Copy

---

## 📝 Reviewer Agent

Reviews all generated outputs and improves:

- Clarity
- Professionalism
- Business Feasibility
- Consistency

---

# Multi-Agent Architecture

```text
User Startup Idea
        ↓
🔍 Market Research Agent
        ↓
📈 Business Strategy Agent
        ↓
🌐 Website Content Agent
        ↓
📢 Marketing Agent
        ↓
📝 Reviewer Agent
        ↓
Final Startup Launch Pack
```

---

# Technical Architecture

The project follows a modular multi-agent architecture.

```text
VIBE_CODING/
│
├── agents/
│   ├── market_research.py
│   ├── business_strategy.py
│   ├── website_content.py
│   ├── marketing.py
│   └── reviewer.py
│
├── utils/
│   └── llm.py
│
├── config.py
├── app.py
├── requirements.txt
└── README.md
```

---

# Technologies Used

- Python 3.14
- Groq API
- Llama 3.3 70B Versatile
- VS Code
- GitHub

---

# Installation

## Clone Repository

```bash
git clone <your-repository-url>
cd VIBE_CODING
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Create Environment File

Create a `.env` file:

```env
GROQ_API_KEY=your_api_key_here
```

---

# Usage

Run the application:

```bash
python app.py
```

Example Input:

```text
Online Bakery in India
```

The system will automatically execute all agents and generate a complete startup launch package.

---

# Example Workflow

```text
Input:
Online Bakery in India

Step 1:
Market Research

Step 2:
Business Strategy

Step 3:
Website Content

Step 4:
Marketing Content

Step 5:
Final Review

Output:
Startup Launch Pack
```

---

# Why Agents?

Each agent has a dedicated responsibility.

This improves:

- Modularity
- Maintainability
- Specialization
- Output Quality

Instead of relying on one large prompt, multiple agents collaborate to solve different parts of the problem.

---

# Future Improvements

- Streamlit Web Interface
- Agent Memory
- PDF Report Generation
- Investor Pitch Deck Generation
- Competitor Analysis Dashboard
- Startup Financial Forecasting
- Multi-LLM Support

---

# Security

- API keys are stored in environment variables.
- `.env` files are excluded using `.gitignore`.
- No credentials are stored in source code.

---

# Author

Srivatsa D Patkar

Built for the Kaggle Vibe Coding Capstone Competition.