from pydantic import BaseModel,EmailStr,Field
from typing import Optional

class Student(BaseModel):
    name:str="ali"
    age:Optional[int]=None
    email:EmailStr
    cgpa:float=Field(gt=0,lt=4,default=3,description="A decimal value representing the cgpa of  student")

new_student={'name':'abdul','age':15,'email':'abc@gmail.com','cgpa':3.75}#}

student=Student(**new_student)

std_dict=dict(student)
print(std_dict['age'])

std_json=student.model_dump_json()
print(std_json)