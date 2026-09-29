LangChain Learning & Practice Repository

Welcome to my LangChain repository! This project documents my journey learning LangChain concepts, building applications using Large Language Models (LLMs), and implementing key tools for generative AI development.

📁 Repository Structure

Below is an overview of the modules and concepts covered in this repository:

LangChain/
├── 1.LLMs/                # Working with standard LLM interfaces
├── 2.ChatModels/          # Chat-based model integration & prompt handling
├── 3.EmbeddedModels/      # Generating and working with text embeddings
├── Chains/                # Sequential, Router, and LCEL Chains
├── Document_Loader/       # Loading data from various file types (PDF, Text, Web, etc.)
├── LLMs_Prompts/          # Prompt Templates, Few-Shot prompts, and dynamic prompting
├── OutputParser/          # Formatting LLM output into structured data (JSON, Pydantic, CSV)
├── Runnables/             # LangChain Expression Language (LCEL) and Runnable primitives
├── TextSplitters/         # Text chunking methods (Recursive, Character, Token, etc.)
└── Typed_dictionary/      # Type safety, data modeling, and schema definitions


🚀 Key Topics & Concepts Covered

1. LLMs & Chat Models

Interfaces for integrating language models.

Managing model parameters like temperature, top_p, and max tokens.

Chat history, system messages, human messages, and AI responses.

2. Embeddings & Vector Representations

Converting text into dense vector representations.

Utilizing embedding models for semantic search and similarity matching.

3. Prompts & Output Parsers

Designing reusable PromptTemplate and ChatPromptTemplate instances.

Few-shot learning examples for better LLM context.

Parsing raw LLM outputs into structured formats like JSON and Python dictionaries.

4. Chains & LCEL (LangChain Expression Language)

Building linear and dynamic execution chains.

Combining model calls, prompt templates, and parsers cleanly using pipe | operators (Runnables).

5. Document Loaders & Text Splitters

Extracting raw data from diverse sources (PDFs, Webpages, TXT).

Splitting long texts efficiently into manageable chunks using Recursive Character and Token Splitters.

🛠️ Getting Started

Prerequisites

Python 3.8+

An API key for your chosen provider (e.g., OpenAI, Anthropic, Google Gemini, HuggingFace)

Installation

Clone the repository:

git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name


Create a virtual environment:

python -m venv venv
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate


Install dependencies:

pip install -r requirements.txt


Set up Environment Variables:
Create a .env file in the root directory and add your API keys:

OPENAI_API_KEY=your_openai_api_key_here
ANTHROPIC_API_KEY=your_anthropic_api_key_here
# Add any other keys needed
