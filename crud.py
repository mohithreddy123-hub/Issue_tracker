from sqlalchemy.orm import Session
from models import Issue
from schemas import IssueCreate


def create_issue(db: Session, issue: IssueCreate):
    db_issue = Issue(
        title=issue.title.strip(),
        description=issue.description.strip(),
        status=issue.status.value
    )
    db.add(db_issue)
    db.commit()
    db.refresh(db_issue)
    return db_issue


def get_all_issues(db: Session):
    return db.query(Issue).all()


def update_issue_status(db: Session, issue_id: int, status: str):
    issue = db.query(Issue).filter(Issue.id == issue_id).first()
    
    if not issue:
        return None

    issue.status = status
    db.commit()
    db.refresh(issue)
    return issue