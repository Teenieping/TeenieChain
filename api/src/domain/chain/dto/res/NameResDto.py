from pydantic import BaseModel


class NameResDto(BaseModel):
    name: str
    