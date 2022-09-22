from sqlalchemy import Column, Integer, String

from api.database import Base


class Movie(Base):
    __tablename__ = "movielist"

    id = Column(
        Integer,
        primary_key=True,
        index=True,
        autoincrement=True,
        nullable=False,
    )
    year = Column(Integer)
    title = Column(String)
    studios = Column(String)
    producers = Column(String)
    winner = Column(String)
