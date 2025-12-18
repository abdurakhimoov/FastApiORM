from sqlalchemy.orm import Session
from schemas import student_schema, group_schema
from db.models import Group
from typing import List, Optional

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