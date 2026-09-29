from langchain_openai import ChatOpenAI
import os
import warnings
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableParallel

load_dotenv()
model = ChatOpenAI(
    model="gpt-oss:120b",
    api_key=os.getenv("OLLAMA_API_KEY"),
    base_url="https://ollama.com/v1",
)


# Model 2
model2 = ChatOpenAI(
    model="gpt-oss:20b",      
    api_key=os.getenv("OLLAMA_API_KEY"),
    base_url="https://ollama.com/v1",
)

parser = StrOutputParser()

prompt1=PromptTemplate(
    template="Generate the short and simple notes of the  the text {text}",
    input_variables=['text']
)
prompt2=PromptTemplate(
    template="Generate the quiz of the {text}",
    input_variables=['text']
)
prompt3=PromptTemplate(
    template="Merge the provided notes and quiz into single document \n notes->{notes} and quiz ->{quiz}",
    input_variables=['notes','quiz']
)

parallel_chain=RunnableParallel(
    {"notes":prompt1|model|parser,
     "quiz":prompt2|model2|parser}
)

merge_chain=prompt3|model|parser

chain=parallel_chain|merge_chain

text=""""Human rights are the basic rights and freedoms that every person has. These rights belong to everyone, no matter their age, gender, religion, race, or nationality. Human rights help people live with dignity, equality, and respect.

Some important human rights include the right to life, the right to education, the right to freedom of speech, and the right to healthcare. Every person also has the right to be treated fairly and to live without discrimination or violence.

Governments and organizations work together to protect human rights. Schools also teach students about these rights so they can respect others and understand their own responsibilities. Every person should respect the rights of others because peace and justice depend on mutual respect.

In conclusion, human rights are essential for a happy and safe society. Everyone should know their rights and help protect the rights of others. By respecting human rights, we can build a better and more peaceful world."""

result=chain.invoke({"text":text})
print(result)