# ReDI School – Agentic AI System Development

![ReDI](assets/redi_banner.png)

This repository contains the course materials for the ReDI School Agentic AI System Development course.

## 📚 Structure

```
Agentic-AI-System-Development
├── README.md
├── syllabus.md
├── classes
│   ├── 01-python-refresher-oop/
│   ├── 02-oop-continued/
│   ├── 03-production-python-intro-llms/
│   ├── 04-llm-applications-structured-output/
│   ├── 05-langchain-langgraph-tools-agents/
│   │   ├── code/
│   │   ├── homework/
│   │   └── resources/
│   └── ...
├── projects
│   └── ...
└── assets
    └── images, PDFs, diagrams, etc.
```

- `classes/`: Contains subfolders for each class, each with `code/`, `homework/`, and `resources/` directories.
- `assets/`: Directory for shared diagrams, PDFs, or other media.

## 📌 Purpose

- Provide students with structured course materials
- Help students navigate content and complete assignments
- Offer code examples and solutions for reference

## 📚 For Students

### How to Work with Course Materials

This repository is **read-only** — you should not edit files directly inside it. This applies to everything: class exercises, notebooks, and homework. Instead, always **copy** the folder you want to work on to somewhere else on your computer and work on the copy.

It's done this way because new material will be added to this repository throughout the course. If you edit files directly in the repo, you won't be able to pull the latest changes without running into conflicts. By keeping your work separate, a simple `git pull` will always work.

Here's the step-by-step workflow:

**1. Pull the latest changes**

```bash
cd path/to/Agentic-AI   # navigate to where you cloned this repo
git pull
```

**2. Copy the folder you want to work on**

**3. Open a terminal in your copied folder and create a virtual environment**

```bash
python -m venv .venv
source .venv/bin/activate        # On Windows: .venv\Scripts\activate
```

**4. Install dependencies**

Each folder that contains code has a `requirements.txt`:

```bash
pip install -r requirements.txt
```

**5. Create your `.env` file**

Many exercises require API keys. Create a `.env` file in your working folder:

```
GROQ_KEY=your-api-key-here
OPENAI_API_KEY=your-api-key-here
OPENAI_ENDPOINT=your-endpoint-here
```

Add whichever keys the exercise requires. **Never hardcode API keys in your code** — always load them from `.env` using `python-dotenv`.

**6. Do your work!**

You now have your own isolated copy with its own virtual environment. You can edit files freely without worrying about the repository.

### Why do it this way?

- Practice your real-world workflow, creating virtual environments, managing dependencies, and keeping your work organized.
- **No conflicts:** When new material is added to the repository, you can simply `git pull` and it will work cleanly because you haven't changed any files in the repo.

## 🗓️ Course Schedule

See the [syllabus.md](./syllabus.md) file for a detailed week-by-week breakdown of topics.

---

❤️ ReDI School – Aarhus

---
