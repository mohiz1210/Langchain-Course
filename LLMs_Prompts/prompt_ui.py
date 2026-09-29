
#static prompts

# from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
# from dotenv import load_dotenv
# import streamlit as st
# load_dotenv()



# llm = HuggingFaceEndpoint(
#     repo_id="meta-llama/Llama-3.1-8B-Instruct"
# )


# model = ChatHuggingFace(llm=llm)

# st.header("Research Tool")

# user_input=st.text_input("Enter your Prompt")

# if st.button('Summarize'):
#     result=model.invoke(user_input)
#     st.write(result.content)#show text on web page

#dynamic prompts

from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
#from langchain_ollama import ChatOllama
from dotenv import load_dotenv
import streamlit as st
from langchain_core.prompts import PromptTemplate,load_prompt

# load_dotenv()

# #Load the Hugging Face model
# llm = HuggingFaceEndpoint(
#     repo_id="meta-llama/Llama-3.1-8B-Instruct"
# )

# model = ChatHuggingFace(llm=llm)
#model = ChatOllama(model="llama3.2")

from langchain_openai import ChatOpenAI
import warnings 
import os 

load_dotenv()

model = ChatOpenAI(
    model="gpt-oss:120b",
    api_key=os.getenv("OLLAMA_API_KEY"),
    base_url="https://ollama.com/v1",
)


st.header("Research Tool")

# User Inputs
paper_input = st.selectbox(
    "Select Research Paper Name",
    [
        "Attention Is All You Need",
        "BERT: Pre-training of Deep Bidirectional Transformers",
        "GPT-3: Language Models are Few-Shot Learners",
        "Diffusion Models Beat GANs on Image Synthesis"
    ]
)

style_input = st.selectbox(
    "Select Explanation Style",
    [
        "Beginner-Friendly",
        "Technical",
        "Code-Oriented",
        "Mathematical"
    ]
)

length_input = st.selectbox(
    "Select Explanation Length",
    [
        "Short (1-2 paragraphs)",
        "Medium (3-5 paragraphs)",
        "Long (Detailed explanation)"
    ]
)

# Prompt Template
template=load_prompt('template.json')

# Generate prompt when button is clicked
if st.button("Summarize"):
    chain = template|model
    result=chain.invoke( {
            "paper_input": paper_input,
            "style_input": style_input,
            "length_input": length_input,
        })
    # prompt = template.invoke(
    #     {
    #         "paper_input": paper_input,
    #         "style_input": style_input,
    #         "length_input": length_input,
    #     }
    # )

    # result = model.invoke(prompt)
    st.write(result.content)