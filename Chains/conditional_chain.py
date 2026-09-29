from langchain_openai import ChatOpenAI
import os
import warnings
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableParallel,RunnableBranch,RunnableLambda
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel,Field
from typing import Literal

load_dotenv()
model = ChatOpenAI(
    model="gpt-oss:120b",
    api_key=os.getenv("OLLAMA_API_KEY"),
    base_url="https://ollama.com/v1",
)

parser=StrOutputParser()

class Feedback(BaseModel):
    sentiment:Literal['positive','negative']=Field(description="give the sentiment of the feedback")


parser2=PydanticOutputParser(pydantic_object=Feedback)

prompt1=PromptTemplate(
    template="Classify  the sentiment of the following feedback into  positive or negative\n {feedback}\n {format_instructions}",
    input_variables=['feedback'],
    partial_variables={'format_instructions':parser2.get_format_instructions()}
)





classifier_chain=prompt1|model|parser2

prompt2=PromptTemplate(
    template="Write an appropriate responce to this positive feedback\n {feedback}",
    input_variables=['feedback']
)

prompt3=PromptTemplate(
    template="Write an appropriate responce to this negative feedback\n {feedback}",
    input_variables=['feedback']
)



branch_chain= RunnableBranch(
    # (condition1,chain1),
    # (condition2,chain2)
    # default cahin
    (lambda x:x.sentiment=="positive",prompt2|model|parser),
    (lambda x:x.sentiment=="negative",prompt3|model|parser),
    RunnableLambda(lambda x:"could not find sentiment")
)

chain=classifier_chain|branch_chain
result=chain.invoke({'feedback':'this is  terrible phone '})
print(result)