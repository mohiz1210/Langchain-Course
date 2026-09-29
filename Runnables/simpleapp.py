from langchain_openai import ChatOpenAI
import os
import warnings
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate


load_dotenv()
model = ChatOpenAI(
    model="gpt-oss:120b",
    api_key=os.getenv("OLLAMA_API_KEY"),
    base_url="https://ollama.com/v1",
)

prompt=PromptTemplate(
    template="Suggest a catchy blog titile about {topic}",
    input_variables=['topic']
)

topic=input('enter a topic:')

formatted_prompt=prompt.format(topic=topic)

response=model.invoke(formatted_prompt)
blog_title=response.content

print('generated blog title:',blog_title)