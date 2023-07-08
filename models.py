
from typing import Optional
from pydantic import BaseModel

class Eduction(BaseModel):
    degree : str
    startYear : Optional[int]
    endYear : int
    marks : float
    institute :str


class User(BaseModel):
    userName: str
    email : str
    password :str
    name : str
    surname : Optional[str]
    middleName : Optional[str]
    education : list[Eduction]
    Totalexperience : float
    recentCompany : str
    phoneNumber : Optional[str]
