import uuid
from typing import List, Any
from fastapi.requests import Request
from fastapi.responses import Response
from fastapi.routing import APIRouter
from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session
from App.Model.account import Accounts
from App.Data.database import get_db
from App.Schema.base.Output import OutputSchema
import random
from datetime import datetime
from App.context.logic import create_account
create_router = APIRouter()



@create_router.post('/new_user', status_code=status.HTTP_201_CREATED)
async def create(account: OutputSchema, db: Session = Depends(get_db)):
      data = create_account(Accounts(), account, db)
      return data



      