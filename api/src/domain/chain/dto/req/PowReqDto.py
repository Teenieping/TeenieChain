from pydantic import BaseModel


class PowReqDto(BaseModel):
    previous_chain: int
    new_proof: int
