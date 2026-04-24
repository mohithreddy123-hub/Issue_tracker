from pydantic import BaseModel
from typing import Optional
from enum import Enum


class StatusEnum(str, Enum):
    Open = "Open"
    In_Progress = "In Progress"
    Closed = "Closed"


class IssueCreate(BaseModel):
    title: str
    description: str
    status: Optional[StatusEnum] = StatusEnum.Open


class IssueResponse(BaseModel):
    id: int
    title: str
    description: str
    status: StatusEnum

    class Config:
        from_attributes = True