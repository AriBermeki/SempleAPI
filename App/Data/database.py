from sqlalchemy import create_engine
from sqlalchemy.orm import relationship, sessionmaker, declarative_base
from decouple import config


DB = config('Database')
USER = config('USER')
PASSWORD = config('PASSWORD')
HOST = config('HOST')
PORT = config('PORT')


#DB_URL = f"postgresql+psycopg2://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB}"
DB_URL = 'sqlite:///base.db'

engine =create_engine(DB_URL, connect_args={"check_same_thread": False}, future=True)

Sessionlocal = sessionmaker(autocommit=False,autoflush=False ,bind=engine, future=True)


Base = declarative_base()

def get_db():
    db = Sessionlocal()
    try:
        yield db
    finally:
        db.close()

