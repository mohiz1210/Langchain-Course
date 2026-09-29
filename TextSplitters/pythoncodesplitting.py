from langchain_text_splitters import RecursiveCharacterTextSplitter,Language
from langchain_community.document_loaders import PyPDFLoader


# loader=PyPDFLoader('OEL(OS).pdf')
# docs=loader.load()

text=""""# Class 1
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Student Name: {self.name}")
        print(f"Student Age: {self.age}")


# Class 2
class Course:
    def __init__(self, course_name, instructor):
        self.course_name = course_name
        self.instructor = instructor

    def display_course(self):
        print(f"Course Name: {self.course_name}")
        print(f"Instructor: {self.instructor}")


# Creating objects
student1 = Student("Ali", 20)
course1 = Course("Python Programming", "Mr. Ahmed")

# Calling methods
student1.display_info()
print()  # Blank line
course1.display_course()"""

splitter=RecursiveCharacterTextSplitter.from_language(
    language=Language.PYTHON,
    chunk_size=100,
    chunk_overlap=0
)
result=splitter.split_text(text)
# result=splitter.split_documents(docs)
print(result[0]) 
print(len(result))