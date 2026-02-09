from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from models import Employee, Attendance
from database import employee_collection, attendance_collection

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# ---------- EMPLOYEE ROUTES ----------

@app.post("/employees")
def add_employee(emp: Employee):
    if employee_collection.find_one({"employeeId": emp.employeeId}):
        raise HTTPException(status_code=400, detail="Employee already exists")
    employee_collection.insert_one(emp.dict())
    return {"message": "Employee added"}

@app.get("/employees")
def get_employees():
    return list(employee_collection.find({}, {"_id": 0}))


# ---------- ATTENDANCE ROUTES ----------

@app.post("/attendance")
def mark_attendance(att: Attendance):
    attendance_collection.insert_one(att.dict())
    return {"message": "Attendance marked"}

@app.get("/attendance/{employeeId}")
def get_attendance(employeeId: str):
    return list(
        attendance_collection.find(
            {"employeeId": employeeId},
            {"_id": 0}
        )
    )
