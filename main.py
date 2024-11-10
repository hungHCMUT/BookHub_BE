from fastapi import FastAPI
import models
from database import engine
from routers import users, books, membership


app = FastAPI()

models.Base.metadata.create_all(bind=engine)


app.include_router(users.router, tags=["users"])
app.include_router(books.router, tags=["books"])
app.include_router(membership.router, tags=["membership"])
