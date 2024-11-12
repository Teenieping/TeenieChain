from pydantic import BaseModel


class GetTotalSupplyResDto(BaseModel):
    supply: str
