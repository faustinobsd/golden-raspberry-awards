from typing import List

from pydantic import BaseModel


class Producer(BaseModel):
    producer: str
    interval: int
    previousWin: int
    followingWin: int


class WinnerIntervals(BaseModel):
    min: List[Producer]
    max: List[Producer]
