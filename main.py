from fastapi import FastAPI, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import Optional

from database import engine, Base, get_db
from schemas import IssueCreate, IssueResponse, StatusEnum
import crud

Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.post("/issues", response_model=IssueResponse, status_code=201)
def create_issue(issue: IssueCreate, db: Session = Depends(get_db)):
    return crud.create_issue(db, issue)


@app.get("/issues", response_model=list[IssueResponse])
def get_issues(
    status: Optional[StatusEnum] = Query(None, description="Filter issues by status"), 
    db: Session = Depends(get_db)
):
    status_value = status.value if status else None
    return crud.get_all_issues(db, status=status_value)


@app.put("/issues/{issue_id}/status", response_model=IssueResponse)
def update_status(issue_id: int, status: StatusEnum, db: Session = Depends(get_db)):
    updated_issue = crud.update_issue_status(db, issue_id, status.value)

    if not updated_issue:
        raise HTTPException(status_code=404, detail="Issue not found")

    return updated_issue