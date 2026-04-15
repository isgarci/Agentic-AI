# Exercise 2 - Try Out Different Model Parameters

## Setup

Create a virtual environment and install the required dependencies (or skip if you already did this for Exercise 1):

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install openai python-dotenv jupyter
```

Create a `.env` file in the homework folder with your API key (skip if you already did this for Exercise 1):

```
GROQ_KEY=your_api_key_here
```

## Instructions

1. Open the Jupyter notebook `exercise2 - model parameters.ipynb`
2. Tweak the parameters of the model (temperature, max_tokens, top_p) and observe how its behavior changes.
