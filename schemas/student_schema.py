from pydantic import BaseModel
from typing import List
from .group_schema import GroupBase


class StudentBase(BaseModel):
    name: str


class StudentCreate(StudentBase):
    pass


class Student(StudentBase):
    id: int
    groups: List["GroupBase"] = []

    class Config:
        from_attributes = True