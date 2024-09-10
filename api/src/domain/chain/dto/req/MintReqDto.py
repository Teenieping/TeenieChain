from pydantic import BaseModel


class MintReqDto(BaseModel):
    previous_hash: int
    proof: int
    transaction: str    # Todo
