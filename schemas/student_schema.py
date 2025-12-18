from pydantic import BaseModel
from typing import List, Optional
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


class StudentUpdate(BaseModel):
    name: Optional[str] = None
    group_ids: Optional[List[int]] = None