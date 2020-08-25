from fastapi import FastAPI

#import database settings
from db import database

#import routes here
from routes import route_wilayah

app = FastAPI()
#Register routes here.
app.include_router(route_wilayah.router, prefix = "/wilayah", tags = ['wilayah'])

# connect to database on startup
@app.on_event("startup")
async def startup():
    await database.connect()

#disconnect database on shutdown
@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


