# Python import
from typing import Optional

# Pydantic imports
from pydantic import Field, BaseModel

class Movie(BaseModel):
    title: str = Field(min_lenght= 5, max_length=15, default= "movie title")
    overview: str = Field(min_length=5, max_length=100, default="movie overview")
    year: int = Field(default=2022, le=2023)
    rating: float = Field(default=1.0, ge=1,le=10)
    category: str = Field(default="category movie")
