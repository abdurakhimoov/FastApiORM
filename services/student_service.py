from sqlalchemy.orm import Session
from schemas import student_schema
from db.models import Student
from typing import List, Optional

def create_student(db: Session, student: student_schema.StudentCreate) -> Student:
    a_student = Student(name=student.name)
    db.add(a_student)
    db.commit()
    db.refresh(a_student)
    return a_student


def get_student(id: int, db: Session) -> Optional[Student]:
    return db.get(Student, id)


def get_all_student(db: Session) -> List[Student]:
    students = db.query(Student).all()
    return students
