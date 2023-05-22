from pydantic import BaseModel, Field


class Movie(BaseModel):
    title: str = Field(max_length=15)
    overview: str = Field(min_length=15, max_length=50)
    year: int = Field(ge=1800)
    rating: float = Field(ge=0, le=10)
    category: str = Field(max_length=15)
