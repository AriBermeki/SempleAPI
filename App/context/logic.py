from fastapi import Depends
from sqlalchemy.orm import Session
from App.Data.database import get_db
import random
from datetime import datetime
from fastapi import HTTPException, status

def create_account(model_name, schema, database_connection):
    new = model_name
    if new is None:
        raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail='Error with code 404 not found'
        )
   
    new.id = random.randint(2202, 3000)
    new.email = schema.email
    new.username = schema.username
    new.email = schema.email
    new.password = schema.password
    new.date_joiend = datetime.utcnow()
    database_connection.add(new)
    database_connection.commit()
    return new
    



def create_profile(model_name, schema, database_connection):
    new = model_name
    if new is None:
        raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail='Error with code 404 not found'
        )
    new.id = random.randint(2202, 3000)
    new.frist_name = schema.frist_name
    new.last_name = schema.last_name
    new.birth_data = schema.birth_data
    new.address = schema.address
    new.apartment_number = schema.apartment_number
    new.zip = schema.zip
    new.city = schema.city
    new.profile_pictor = schema.profile_pictor
    new.avatar = schema.avatar
    new.bio = schema.bio
   
    database_connection.add(new)
    database_connection.commit()
    return new
    



def create_circls(model_name, schema, database_connection):
    new = model_name
    if new is None:
        raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail='Error with code 404 not found'
        )
    new.id = random.randint(2202, 3000)
    new.name = schema.name
    new.description = schema.description
    new.creator_id = schema.creator_id
    new.members = schema.members
    new.image = schema.image
    database_connection.add(new)
    database_connection.commit()
    return new
    


def create_connections(model_name, schema, database_connection):
    new = model_name
    if new is None:
        raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail='Error with code 404 not found'
        )
    new.id = random.randint(2202, 3000)
    new.sender_id = random.randint(2202, 3000)
    new.receiver_id = random.randint(2202, 3000)
    database_connection.add(new)
    database_connection.commit()
    return new
    


def create_message(model_name, schema, database_connection):
    new = model_name
    if new is None:
        raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail='Error with code 404 not found'
        )
    new.id = random.randint(2202, 3000)
    new.sender_id = random.randint(2202, 3000)
    new.receiver_id = random.randint(2202, 3000)
    new.message= schema.message
    database_connection.add(new)
    database_connection.commit()
    return new
    


def create_post(model_name, schema, database_connection):
    new = model_name
    if new is None:
        raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail='Error with code 404 not found'
        )
    new.id = random.randint(2202, 3000)
    new.circle_id = random.randint(2202, 3000)
    new.user_id = random.randint(2202, 3000)
    new.date = datetime.date()
    new.time = datetime.time()
    database_connection.add(new)
    database_connection.commit()
    return new
    

def create_reaction(model_name, schema, database_connection):
    new = model_name
    if new is None:
        raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail='Error with code 404 not found'
        )
    new.id = random.randint(2202, 3000)
    new.post_id = random.randint(2202, 3000)
    new.user_id = random.randint(2202, 3000)
    new.type = schema.type
    database_connection.add(new)
    database_connection.commit()
    return new
    


def create_comment(model_name, schema, database_connection):
    new = model_name
    if new is None:
        raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail='Error with code 404 not found'
        )
    new.id = random.randint(2202, 3000)
    new.post_id = random.randint(2202, 3000)
    new.user_id = random.randint(2202, 3000)
    new.content = schema.content
    new.date = datetime.date()
    new.time = datetime.time()
    database_connection.add(new)
    database_connection.commit()
    return new
    

def delete_data(id, model_name, database_connection):
    data = database_connection.query(model_name).filter(model_name.id==id).delete()
    database_connection.commit()
    return data
    

def read_all(model_name, database_connection):
    data = database_connection.query(model_name).all()
    return data
    

def read_by_id(id, model_name, database_connection):
    data = database_connection.query(model_name).filter(model_name.id==id).first()
    return data


def update_account_data(id, model_name, schema, database_connection):
    data = database_connection.query(model_name).filter(model_name.id==id).first()
    if schema is None:
        raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail='Error with code 404 not found'
    )
    data.email = schema.email
    data.username = schema.username
    data.email = schema.email
    data.password = schema.password
    database_connection.add(data)
    database_connection.commit()
    return f'The User:  {data} with the  ID: {id} has been Successfuly Updated'
    


 
    