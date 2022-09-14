import uuid
from fastapi import Depends, HTTPException, status
from fastapi.routing import APIRouter
from fastapi.requests import Request
from fastapi.responses import Response
from App.Model.account import Accounts
from App.Data.database import get_db
from App.Schema.base.Output import OutputSchema
from App.context.logic import update_account_data
from sqlalchemy.orm import Session
update_router = APIRouter()


@update_router.put('/update_user/{user_id}', status_code=status.HTTP_202_ACCEPTED)   
async def update(user_id: int, account: OutputSchema, db: Session = Depends(get_db)):

    #____________ Hier wird untersucht, ob die Output Daten gleich der Input is ______________#


    data = update_account_data(user_id,Accounts,account,db)
    return data
    
    
   