import datetime

from pydantic import BaseModel


class QuestionBase(BaseModel):
    id_qst: int
    text_qst: str
    text_ans: str
    created: datetime.date

    class Config:
        orm_mode = True


class Question(QuestionBase):
    id: int

    class Config:
        orm_mode = True

class QuestionCreate(QuestionBase):
    pass
