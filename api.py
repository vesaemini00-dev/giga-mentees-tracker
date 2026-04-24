from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, EmailStr
from queries import create_mentee, list_mentees, update_mentee, delete_mentee

app = FastAPI()


class MenteeCreate(BaseModel):
    full_name: str
    email: EmailStr
    cohort: str


class MenteeUpdate(BaseModel):
    cohort: str


@app.get("/")
def root():
    return {"message": "API is working"}


@app.get("/mentees")
def get_mentees():
    return list_mentees()


@app.post("/mentees", status_code=status.HTTP_201_CREATED)
def add_mentee(mentee: MenteeCreate):
    mentee_id = create_mentee(mentee.full_name, mentee.email, mentee.cohort)
    return {"id": mentee_id}


@app.put("/mentees/{mentee_id}")
def update(mentee_id: int, data: MenteeUpdate):
    updated = update_mentee(mentee_id, data.cohort)
    if not updated:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Mentee {mentee_id} not found"
        )
    return {"updated": True}


@app.delete("/mentees/{mentee_id}")
def delete(mentee_id: int):
    deleted = delete_mentee(mentee_id)
    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Mentee {mentee_id} not found"
        )
    return {"deleted": True}