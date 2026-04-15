# Homework 5: Build Your Own Multi-Tool Agent

## Setup

```bash
pip install -r requirements.txt
```

Create a `.env` file with your API credentials:

```
OPENAI_API_KEY=your-api-key-here
OPENAI_ENDPOINT=your-endpoint-here
```

**Never hardcode API keys in your code.**

---

## Exercise 1: Customer Support Agent

Build a customer support agent for an online store called **"TechBuy"** that sells electronics.

### Requirements

Create an agent with the following **three tools**:

1. **`check_order_status`** — Takes an `order_id` (str) and returns the order status. Use this hardcoded data:
   ```python
   orders = {
       "ORD-001": "Shipped — arriving April 18",
       "ORD-002": "Processing — expected to ship April 16",
       "ORD-003": "Delivered on April 10",
       "ORD-042": "Cancelled — refund issued",
   }
   ```
   Return `"Order not found"` for unknown IDs.

2. **`check_return_eligibility`** — Takes a `product_name` (str) and `days_since_purchase` (int). Returns whether the item is eligible for return (eligible if purchased within 30 days).

3. **`get_store_hours`** — Takes no arguments. Returns the store hours: `"Monday–Friday: 9:00–18:00, Saturday: 10:00–16:00, Sunday: Closed"`.

### Agent setup

- Give the agent a **system prompt** that makes it a friendly, professional customer support representative for TechBuy
- The agent should use the tools when relevant and answer general questions directly

### Test your agent

Try these queries and verify the agent picks the right tool each time:

1. `"Where is my order ORD-001?"`
2. `"I bought a keyboard 45 days ago, can I return it?"`
3. `"What are your store hours?"`
4. `"I bought headphones 2 weeks ago and they broke. Can I return them?"`
5. `"What payment methods do you accept?"` (no tool needed)

Print the full message flow for at least one query (using `msg.pretty_print()`) so you can see the Human → AI → Tool → AI pattern.

---

## Exercise 2: Structured Output + Tools — Job Application Screener

Build an agent that reads a short job application text and returns a **structured evaluation**.

### Define a Pydantic schema

```python
class ApplicationReview(BaseModel):
    applicant_name: str
    years_of_experience: int
    skills: list[str]
    recommendation: str  # "interview", "maybe", or "reject"
    summary: str
```

### Create a tool

**`check_skill_demand`** — Takes a `skill` (str) and returns whether it's currently in high demand. Use this hardcoded data:

```python
high_demand = ["python", "react", "aws", "kubernetes", "langchain", "sql"]
```

Return `"<skill> is in HIGH demand"` if the skill is in the `high_demand` list, or `"<skill> is in normal demand"` otherwise.

### Agent setup

- Give the agent a system prompt: it's a hiring assistant for a tech company
- It should use the `check_skill_demand` tool to look up the applicant's key skills before making a recommendation
- It must return a structured `ApplicationReview`

### Test your agent

Try with at least two different application texts, for example:

```
"Hi, my name is Sarah Chen. I have 5 years of experience in software development.
I'm proficient in Python, React, and AWS. I've led a team of 3 developers and
shipped two production applications. I'm looking for a senior developer role."
```

```
"My name is Jake. I just graduated and I know a bit of HTML and CSS.
I'm looking for any job in tech."
```

Print the structured response fields for each.

---

## Bonus: Conversation Memory

Take your customer support agent from Exercise 1 and have a **multi-turn conversation** with it. Send multiple messages in sequence and verify that the agent remembers context from earlier in the conversation.

Hint: after each `invoke`, take the messages from the result and include them in the next call:

```python
# First turn
result = agent.invoke({"messages": "Where is my order ORD-001?"})
conversation = result["messages"]

# Second turn — pass the full conversation history
conversation.append(HumanMessage("And when exactly will it arrive?"))
result = agent.invoke({"messages": conversation})
```

Verify that the agent answers the follow-up using context from the first exchange.
