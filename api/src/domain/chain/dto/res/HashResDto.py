from pydantic import BaseModel


class HashResDto(BaseModel):
    hash: str
