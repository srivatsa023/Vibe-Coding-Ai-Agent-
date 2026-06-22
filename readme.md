# 🚀 LaunchPilot AI

LaunchPilot AI is a Multi-Agent AI Startup Generator that transforms a startup idea into a complete startup launch package using multiple AI agents powered by Groq LLM.

---

## 🌟 Features

* 🔍 Market Research Agent
* 📊 SWOT Analysis Agent
* 💰 Investor Pitch Agent
* 📈 Business Strategy Agent
* 🌐 Website Content Agent
* 📢 Marketing Agent
* 📝 Reviewer Agent
* 📄 TXT Report Export
* 📄 PDF Report Export

---

## 🏗️ Architecture

User Startup Idea

↓

Market Research Agent

↓

SWOT Agent

↓

Investor Pitch Agent

↓

Business Strategy Agent

↓

Website Content Agent

↓

Marketing Agent

↓

Reviewer Agent

↓

Startup Launch Pack

↓

TXT Report + PDF Report

---

## 📂 Project Structure

VIBE CODING/

├── agents/

│ ├── market_research.py

│ ├── swot.py

│ ├── investor_pitch.py

│ ├── business_strategy.py

│ ├── website_content.py

│ ├── marketing.py

│ └── reviewer.py

│

├── utils/

│ ├── llm.py

│ └── pdf_export.py

│

├── docs/

│ ├── architecture.md

│ ├── demo_script.md

│ └── project_writeup.md

│

├── reports/

├── tests/

├── app.py

├── config.py

├── requirements.txt

└── README.md

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/srivatsa023/Vibe-Coding-Ai-Agent-.git
cd Vibe-Coding-Ai-Agent-
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Configure API Key

Create a `.env` file:

```env
GROQ_API_KEY=your_groq_api_key_here
```

---

## ▶️ Run Project

```bash
python app.py
```

Example:

```text
Enter Startup Idea:
Online Bakery in India
```

---

## 📄 Output

LaunchPilot AI generates:

* Market Research Report
* SWOT Analysis
* Investor Pitch
* Business Strategy
* Website Content
* Marketing Content
* AI Review

Saved as:

```text
startup_report.txt
startup_report.pdf
```

---

## 🛠️ Tech Stack

* Python
* Groq API
* Llama 3.3 70B Versatile
* ReportLab
* Git & GitHub

---

## 👨‍💻 Author

Srivatsa D Patkar

---

## 📜 License

This project is created for educational and portfolio purposes.
