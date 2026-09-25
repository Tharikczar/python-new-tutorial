from fastapi import FastAPI
from .databases import database


app = FastAPI()

# Create tables when the app starts
@app.on_event("startup")
def startup_event():
    database.Base.metadata.create_all(bind=database.engine)
