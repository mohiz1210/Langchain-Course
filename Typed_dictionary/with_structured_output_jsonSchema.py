from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from pydantic import BaseModel,Field
from typing import Literal
import os


load_dotenv()

model = ChatOpenAI(
    model="gpt-oss:120b",
    api_key=os.getenv("OLLAMA_API_KEY"),
    base_url="https://ollama.com/v1",
)

json_schema={
  "title": "Review",
  "type": "object",
  "properties": {
    "summary": {
      "title": "Summary",
      "type": "string",
      "description": "A brief summary of the review"
    },
    "sentiment": {
      "title": "Sentiment",
      "type": "string",
      "enum": [
        "pos",
        "neg"
      ],
      "description": "Return the sentiment of the review"
    }
  },
  "required": [
    "summary",
    "sentiment"
  ]
}
structured_model=model.with_structured_output(json_schema)

result=structured_model.invoke("The hardware is great, but the software feels bloated. There are too many pre-installed apps that I can't remove. Also, the UI looks outdated compared to other brands. Hoping for a software update to fix this.")
print(result)