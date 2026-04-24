from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from database import engine, Base, get_db
from schemas import IssueCreate, IssueResponse, StatusEnum
import crud

Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.post("/issues", response_model=IssueResponse, status_code=201)
def create_issue(issue: IssueCreate, db: Session = Depends(get_db)):
    return crud.create_issue(db, issue)


@app.get("/issues", response_model=list[IssueResponse])
def get_issues(db: Session = Depends(get_db)):
    return crud.get_all_issues(db)


@app.put("/issues/{issue_id}/status", response_model=IssueResponse)
def update_status(issue_id: int, status: StatusEnum, db: Session = Depends(get_db)):
    updated_issue = crud.update_issue_status(db, issue_id, status.value)

    if not updated_issue:
        raise HTTPException(status_code=404, detail="Issue not found")

    return updated_issue