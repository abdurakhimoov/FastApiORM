from pydantic import BaseModel
from typing import List, Optional
from .student_schema import StudentBase


class GroupBase(BaseModel):
    group_name: str


class GroupCreate(GroupBase):
    pass


class Group(GroupBase):
    id: int
    students: List["StudentBase"] = []

    class Config:
        from_attributes = True


class GroupUpdate(BaseModel):
    group_name: Optional[str] = None
    student_ids: Optional[List[int]] = None