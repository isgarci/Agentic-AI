# Exercise 1 - Practice using the API for Large Language Models

## Setup

Create a virtual environment and install the required dependencies:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install openai python-dotenv colorama
```

Create a `.env` file in the homework folder with your API key:

```
GROQ_KEY=your_api_key_here
```

## Instructions

Open `exercise1 - api usage.py` and implement the three classification functions. After implementing them, run the file to test your solutions:

```bash
python "exercise1 - api usage.py"
```

## Sentiment Analysis

A common problem in e-commerce is not having measurable metrics of customer sentiment about products. While star ratings provide some insight, they don't capture the opinions expressed in written reviews. Understanding sentiment at scale allows businesses to identify common issues, highlight the most liked features and get a better understanding of the public's perception of the product.

Your task is to build a system that takes a review of a product as input and classifies the sentiment into 3 categories:

- Positive
- Neutral
- Negative

## E-mail Classification

Many organizations receive thousands of e-mails per day. Manually sorting these e-mails to their correct recipient is both expensive and time consuming.

Your task is to build a system that takes a raw e-mail as input and returns the queue of the department that the e-mail should be routed to:

- "Sales and Pre-Sales"
- "IT Support"
- "Returns and Exchanges"
- "Human Resources"

## Content Moderation System

Online platforms and communities face constant challenges with user-generated content that may violate community guidelines. Simple filters also provide poor protection or produce too many false positives.

Your task is to build a content moderation system that takes in user message as an input and, based on its contents, decides whether the message should be shown or filtered by returning either "allowed" or "filtered".

_Sources: Product review dataset: Hugging Face, Kenneth12/productreviewsentiment_
