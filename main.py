from fastapi.routing import APIRoute
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from App.Router.create import create_router
from App.Router.delete import delete_router
from App.Router.read import reade_router_1, reade_router_2
from App.Router.update import update_router




from decouple import config
app = FastAPI(
    title="GoQuanto is a Scientific  Platform",
    description="Mathematics  Physics  Chemistry",
    version="0.0.1",
    contact={
        "Organisation Name":"GoQuanto is a Scientific  Platform",
        "CTO Email": 'ari.bermeki@icloud.com',
        "Organisation Address":"Germany, Berlin"
    },
    license_info={
        "name":"MIT"
    }
)

app.include_router(create_router)
app.include_router(delete_router)
app.include_router(reade_router_1)
app.include_router(reade_router_2)
app.include_router(update_router)
