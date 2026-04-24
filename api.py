from fastapi import FastAPI
from queries import create_mentee, list_mentees, update_mentee, delete_mentee

app = FastAPI()


@app.get("/")
def root():
    return {"message": "API is working"}


@app.get("/mentees")
def get_mentees():
    return list_mentees()


@app.post("/mentees")
def add_mentee(full_name: str, email: str, cohort: str):
    mentee_id = create_mentee(full_name, email, cohort)
    return {"id": mentee_id}


@app.put("/mentees/{mentee_id}")
def update(mentee_id: int, cohort: str):
    updated = update_mentee(mentee_id, cohort)
    return {"updated": updated}


@app.delete("/mentees/{mentee_id}")
def delete(mentee_id: int):
    deleted = delete_mentee(mentee_id)
    return {"deleted": deleted}