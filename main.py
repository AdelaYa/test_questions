from typing import List

import requests
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

import schemas

from database import engine, get_db
import models
from repositories import QuestionRepo
app = FastAPI()

models.Base.metadata.create_all(bind=engine)


# testing
@app.get("/", tags=["test"])
def greet():
    return {"hello": "world!."}


@app.get('/questions', tags=["questions"], response_model=List[schemas.Question])
def get_all_questions(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """
    Get all Questions in database
    """
    all_questions = QuestionRepo.fetch_all(db, skip=skip, limit=limit)
    return all_questions


@app.post("/question", tags=["question"],  status_code=201)
def add_question(questions_num: int, db: Session = Depends(get_db)):


    try:
        prev_qst = QuestionRepo.get_questions(db)
        result = schemas.Question(
            id=prev_qst[0].id,
            id_qst=prev_qst[0].id_qst,
            text_qst=prev_qst[0].text_qst,
            text_ans=prev_qst[0].text_ans,
            created=prev_qst[0].created,
        )
    except:
        result = models.Question()

    def get_qst():
        list_text = requests.get(f'https://jservice.io/api/random?count={questions_num}').json()
        return list_text

    def check_qst(question):
        qst_exist = QuestionRepo.fetch_by_id_qst(db, question["id"])
        if qst_exist:
            new_qst = get_qst()
            return check_qst(new_qst)
        return question

    for question in get_qst():
        current_qst = check_qst(question)

        db_question = models.Question(
            id_qst=current_qst["id"],
            text_qst=current_qst["question"],
            text_ans=current_qst["answer"],
            created=current_qst["created_at"],
        )
        db.add(db_question)
        db.commit()
        db.refresh(db_question)
    return result
