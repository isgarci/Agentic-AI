import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

#endpoint = "https://foundry-class-group3.cognitiveservices.azure.com/openai/v1/"
#model_name = "gpt-5.4-mini"
model_name = os.environ.get("GPT_MODEL");
deployment_name = os.environ.get("DEPLOYMENT_NAME");
#deployment_name = "model-group3"

client = OpenAI(
    api_key=os.environ.get("AZURE_OPEN_API_BASE_URL"),
    base_url=os.environ.get("AZURE_MODEL_API_KEY"),
)


completion = client.chat.completions.create(
    model=model_name,
    messages=[
        {
            "role": "user",
            "content": "What is the capital of France?",
        }
    ],
)

print(completion.choices[0].message)