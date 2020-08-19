from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import reconstructor

from app.models.base import Base


class Assignment(Base):
    id = Column(Integer, primary_key=True)
    title = Column(String(63))
    due = Column(String(63))
    course_cid = Column(Integer, ForeignKey('course.cid'))

    @reconstructor
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields = ['id', 'title', 'due']