from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain.output_parsers import StructuredOutputParser, ResponseSchema
import os

load_dotenv()

model = ChatOpenAI(
    model="gpt-oss:120b",
    api_key=os.getenv("OLLAMA_API_KEY"),
    base_url="https://ollama.com/v1",
)

schema = [
    ResponseSchema(name="fact1", description="Fact no 1 of the topic"),
    ResponseSchema(name="fact2", description="Fact no 2 of the topic"),
    ResponseSchema(name="fact3", description="Fact no 3 of the topic"),
]

parser = StructuredOutputParser.from_response_schemas(schema)

template = PromptTemplate(
    template="""Give 3 facts about {topic}

{format_instructions}
""",
    input_variables=["topic"],
    partial_variables={
        "format_instructions": parser.get_format_instructions()
    },
)

chain = template | model | parser

result = chain.invoke({"topic": "Black Hole"})
print(result)