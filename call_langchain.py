import os
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

print(base_url := os.getenv("AZURE_OPEN_API_BASE_URL")
      , api_key := os.getenv("AZURE_MODEL_API_KEY")
      , model := os.getenv("DEPLOYMENT_NAME")
      )
llm = ChatOpenAI(
    base_url=os.getenv("AZURE_OPEN_API_BASE_URL"),
    api_key=os.getenv("AZURE_MODEL_API_KEY"),
    model=os.getenv("DEPLOYMENT_NAME")
)


print(llm.invoke("What is the capital of France?"))
"""response = client.chat.completions.create(
    model=os.environ.get("DEPLOYMENT_NAME"),
"""
"""
completion = llm.chat.completions.create(
    model=os.getenv("DEPLOYMENT_NAME"),
    messages=[
        {
            "role": "user",
            "content": "What is the capital of France?",
        }
    ],
)
"""
