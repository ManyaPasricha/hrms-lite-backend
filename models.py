from pydantic import BaseModel, EmailStr

class Employee(BaseModel):
    employeeId: str
    name: str
    email: EmailStr
    department: str

class Attendance(BaseModel):
    employeeId: str
    date: str
    status: str
