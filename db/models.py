from sqlalchemy import Column, Table, ForeignKey, String, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .databse import Base
from typing import List


student_group_association = Table(
    "student_group",
    Base.metadata,
    Column("student_id", ForeignKey("students.id"), primary_key=True),
    Column("group_id", ForeignKey("groups.id"), primary_key=True),
)


class Student(Base):
    __tablename__ = "students"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(100))

    groups: Mapped[List["Group"]] = relationship(
        secondary=student_group_association, back_populates="students"
    )

    def __repr__(self):
        return f"Student(id={self.id}, name='{self.name}')"


class Group(Base):
    __tablename__ = "groups"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    group_name: Mapped[str] = mapped_column(String(50))

    students: Mapped[List["Student"]] = relationship(
        secondary=student_group_association, back_populates="groups"
    )

    def __repr__(self):
        return f"Group(id={self.id}, name='{self.group_name}')"