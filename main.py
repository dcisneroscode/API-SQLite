# My imports
from config.database import engine, Base
from middlewares.error_handler import Error_Handler
from routers.movie import movie_router


# FastAPI imports
from fastapi import FastAPI



app = FastAPI()
app.title = "Movie API connect with Database"
app.version = "0.0.1"
app.add_middleware(Error_Handler)
app.include_router(movie_router)

Base.metadata.create_all(bind=engine)




    