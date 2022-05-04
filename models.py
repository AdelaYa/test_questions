from sqlalchemy import Column, Integer, String, DateTime
import datetime
from database import Base


class Question(Base):
    __tablename__ = "question"

    id = Column(Integer, primary_key=True, index=True)
    id_qst = Column(Integer)
    text_qst = Column(String)
    text_ans = Column(String)
    created = Column(DateTime, default=datetime.datetime.utcnow())

    def __repr__(self):
        return 'Question(text_qst=%s, text_ans=%s, created=%s)' % (self.text_qst, self.text_ans, self.created)

