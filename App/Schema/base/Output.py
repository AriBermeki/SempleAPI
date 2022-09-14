import typing
from uuid import UUID
from pydantic import BaseModel, EmailStr, Field
import random
from datetime import datetime
from typing import Optional
from enum import Enum

class Role(Enum):
    is_active = 'is_active'
    is_staff = 'is_staff'


class OutputSchema(BaseModel):
    id: int            = random.randint(2202,3000)
    email: EmailStr
    username: str
    password: str
    date_joiend: datetime
    role: Optional[Role] = None

    class Config:
        orm_mode = True



class ProfileSchema(BaseModel):
    id: int
    first_name: str
    last_name: str
    birth_data: Optional[datetime] = None
    address: Optional[str] = None
    apartment_number: Optional[int] = None
    zip: Optional[int] = None
    city: Optional[str] = None
    profile_pictor: Optional[str] = None
    avatar: Optional[str] = None
    bio: Optional[str] = None

    class Config:
        orm_mode = True

  