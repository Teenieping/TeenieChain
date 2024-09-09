from pydantic import BaseModel


class BlockReqDto(BaseModel):
    block: str
