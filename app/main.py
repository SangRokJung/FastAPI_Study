from fastapi import FastAPI, HTTPException
from starlette.responses import Response

from app.db.models import UserAnswer
from app.api import api

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Fast API in Python"}


@app.get("/user")
def read_user():
    return api.read_user()

# @app.get("/")
# async def read_all_male(skip_male: Optional[str] = None):
#     if skip_male :
#         new_males = MALES.copy()
#         del new_males[skip_male]
#         return new_males
#     return MALES

