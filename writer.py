import os
from datetime import datetime

OUTPUT_DIR = "proposals"

os.makedirs(OUTPUT_DIR, exist_ok=True)


def generate_proposal(job_title, job_url):
    today = datetime.now().strftime("%Y-%m-%d")

    text = f"""
Application Date: {today}

Role: {job_title}
Source: {job_url}

---

Why I Fit This Role:

I specialize in automation-first engineering workflows.
My focus is reducing manual operations using Python, APIs, and AI tooling.

Recently I built systems that:
• Automatically discover remote opportunities
• Extract structured data from live job markets
• Build execution pipelines instead of manual work

This role aligns strongly with my background in:
Python automation
AI-assisted development
Data pipeline integration
Remote-first async collaboration

---

What I Can Deliver Fast:

• Production-grade Python scripting
• API integrations
• Workflow automation
• Data handling & transformation
• AI tooling integration

I focus on shipping working solutions, not theory.

---

Availability:
Immediate.

Open to trial task to demonstrate capability.
"""

    safe_name = job_title.replace("/", "").replace("\\", "")[:40]
    filename = f"{OUTPUT_DIR}/{safe_name}.txt"

    with open(filename, "w", encoding="utf-8") as f:
        f.write(text)

    print("Generated proposal:", filename)
