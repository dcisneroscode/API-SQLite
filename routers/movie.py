# My imports
from models.movie import MovieModel
from config.database import Session
from services.movie import MovieServices
from schemas.movie import Movie

# FastAPI imports
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

movie_router = APIRouter()

@movie_router.get(
        path="/movies",
        tags=["movies"],
        status_code= 200
)
def movies():
    db = Session()
    result = MovieServices(db).get_movies()
    return JSONResponse(status_code=200, content=jsonable_encoder(result))



@movie_router.get(
        path="/movies/{id}",
        tags=["movies"],
        status_code= 200
)
def movie_by_id(id: int):
    db = Session()
    result = MovieServices(db).get_movie(id)
    if not result:
        return JSONResponse(status_code=404, content={"message" : "not found"})
    return JSONResponse(status_code=200, content=jsonable_encoder(result))



@movie_router.post(
    path="/movies",
    tags=["movies"],
    response_model= dict,
    status_code=200
)
def create_movie(movie: Movie) -> dict:
    db = Session()
    MovieServices(db).create_movie(movie)
    return JSONResponse(status_code=201, content={"message" : "created sucessfull"})


@movie_router.put(
        path="/movies/{id}",
        tags=["movies"],
        status_code=200
)
def update_movie(id: int, movie: Movie):
    db = Session()
    result = MovieServices(db).get_movie(id)
    if not result:
        return JSONResponse(status_code=404, content={"message" : "not found"})
    MovieServices(db).update_movie(id, movie)
    return JSONResponse(status_code=200, content={"message" : "update succesfull"})



@movie_router.delete(
    path="/movies/{id}",
    tags=["movies"],
    status_code=200
)
def delete_movie(id: int):
    db = Session()
    result = MovieServices(db).get_movie(id)
    MovieServices(db).delete_movie(id)
    if not result:
        JSONResponse(status_code=404, content={"message" : "not found"})
    return JSONResponse(status_code=200, content={"message" : "delete succesfull"})