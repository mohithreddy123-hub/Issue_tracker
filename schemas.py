from pydantic import BaseModel, Field
from typing import Optional
from enum import Enum

class StatusEnum(str, Enum):
    Open = "Open"
    In_Progress = "In Progress"
    Closed = "Closed"

class IssueCreate(BaseModel):
    title: str = Field(..., min_length=1, description="The title of the issue")
    description: str = Field(..., min_length=1, description="Detailed description of the issue")
    status: StatusEnum = StatusEnum.Open

class IssueResponse(BaseModel):
    id: int
    title: str
    description: str
    status: StatusEnum

    class Config:
        from_attributes = True