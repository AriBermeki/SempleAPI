from typing import List, Union
import uuid
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException, status
from fastapi.routing import APIRouter
from fastapi.requests import Request
from fastapi.responses import Response
from App.Model.account import Accounts
from App.Data.database import get_db
from App.Data.database import Sessionlocal
from App.Schema.base.Output import OutputSchema
from App.context.logic import read_all, read_by_id


reade_router_1 = APIRouter()
reade_router_2 = APIRouter()

@reade_router_1.get('/reade_user')
async def read_data(db: Session = Depends(get_db)):
    data = read_all(Accounts,db)
    return data



@reade_router_1.get('/reade_user/{user_id}')
async def read_data(user_id: int, db: Session = Depends(get_db)):
    data = read_by_id(user_id, Accounts,db)
    return data
