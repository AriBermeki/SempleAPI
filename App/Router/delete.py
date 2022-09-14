import uuid
from fastapi import Depends, HTTPException, status
from fastapi.routing import APIRoute, APIRouter
from fastapi.requests import Request
from fastapi.responses import Response
from App.Model.account import Accounts
from App.Data.database import get_db
from App.Schema.base.Output import OutputSchema
from sqlalchemy.orm import Session
from App.context.logic import delete_data


delete_router = APIRouter()


@delete_router.delete('/delete_user/{user_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete(user_id: int, db: Session = Depends(get_db)):
        #____________ Hier wird untersucht, ob die Output ID gleich der Input ID ist, wenn ja, dann wird die daten aus der Daten Bank gelöscht, wenn nicht wird eine Fehle zurück gegeben , dass diese eingegebene ID nicht exestiert ist______________#
        data = delete_data(user_id, Accounts,db)
        return data
      