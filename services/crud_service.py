from sqlalchemy.orm import Session
from schemas import student_schema, group_schema
from db.models import Student, Group
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


def update_student(db: Session, student_id: int, student_data: student_schema.StudentUpdate):
    db_student = db.get(Student, student_id)
    if not db_student:
        return None

    if student_data.name is not None:
        db_student.name = student_data.name

    if student_data.group_ids is not None:
        new_groups = db.query(Group).filter(Group.id.in_(student_data.group_ids)).all()
        db_student.groups = new_groups

    db.commit()
    db.refresh(db_student)
    return db_student


def create_group(db: Session, group: group_schema.GroupCreate) -> Group:
    db_group = Group(group_name=group.group_name)
    db.add(db_group)
    db.commit()
    db.refresh(db_group)
    return db_group


def get_group(db: Session, group_id: int) -> Optional[Group]:
    return db.get(Group, group_id)


def get_all_groups(db: Session) -> List[Group]:
    return db.query(Group).all()


def update_group(db: Session, group_id: int, group_data: group_schema.GroupUpdate):
    db_group = db.get(Group, group_id)
    if not db_group:
        return None

    if group_data.group_name is not None:
        db_group.group_name = group_data.group_name

    if group_data.student_ids is not None:
        new_students = db.query(Student).filter(Student.id.in_(group_data.student_ids)).all()
        db_group.students = new_students

    db.commit()
    db.refresh(db_group)
    return db_group


def add_student_to_group(db: Session, student_id: int, group_id: int) -> Optional[Student]:
    """Talabani guruhga qo'shish (Many-to-Many bog'lanish yaratish)."""
    
    # 1. Ikkala ob'ektni ham bazadan qidiramiz
    student = db.get(Student, student_id)
    group = db.get(Group, group_id)
    
    # 2. Agar ikkalasi ham mavjud bo'lsa
    if student and group:
        # 3. SQLAlchemy mo'jizasi: shunchaki ro'yxatga append qilamiz
        # Agar talaba allaqachon guruhda bo'lsa, qayta qo'shmaslik uchun tekshiramiz
        if group not in student.groups:
            student.groups.append(group)
            db.commit()
            db.refresh(student)
        return student
        
    return None # Talaba yoki guruh topilmasa