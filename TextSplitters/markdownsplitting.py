from langchain_text_splitters import RecursiveCharacterTextSplitter,Language
from langchain_community.document_loaders import PyPDFLoader


# loader=PyPDFLoader('OEL(OS).pdf')
# docs=loader.load()

text=""""# The Beauty of Nature

Nature is one of the greatest gifts to humanity. It provides us with clean air, fresh water, food, and beautiful landscapes. Mountains, rivers, forests, and oceans all contribute to the balance of life on Earth.

## Why Nature is Important

- 🌳 Produces oxygen for living beings.
- 💧 Supplies fresh water.
- 🐦 Provides habitats for animals and birds.
- 🌍 Helps maintain ecological balance.

## Ways to Protect Nature

1. Plant more trees.
2. Reduce plastic waste.
3. Save water and electricity.
4. Recycle and reuse materials.
5. Protect wildlife and forests.

> "The Earth does not belong to us; we belong to the Earth."

### Sample Python Code

```python
def greet():
    print("Protect Nature, Protect Life!")

greet()
```

### Conclusion

Taking care of nature today ensures a healthier and greener planet for future generations."""

splitter=RecursiveCharacterTextSplitter.from_language(
    language=Language.MARKDOWN,
    chunk_size=100,
    chunk_overlap=0
)
result=splitter.split_text(text)
# result=splitter.split_documents(docs)
print(result[0]) 
print(len(result))