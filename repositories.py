from sqlalchemy.orm import Session

import models
import schemas


class QuestionRepo:

    async def create(db: Session, question: schemas.QuestionBase):
        db_question = models.Question(text_qst=question.text_qst, text_ans=question.text_ans)
        db.add(db_question)
        db.commit()
        db.refresh(db_question)
        return db_question

    def fetch_by_id_qst(db: Session, id_qst: object):
        return db.query(models.Question).filter(models.Question.id_qst == id_qst).first()

    def fetch_all(db: Session, skip: int = 0, limit: int = 100):
        return db.query(models.Question).offset(skip).limit(limit).all()

    def get_questions(db: Session):
        return db.query(models.Question).order_by(models.Question.id.desc()).all()



