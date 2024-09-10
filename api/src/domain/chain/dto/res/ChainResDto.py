from pydantic import BaseModel

from TeenieChain.Block import Block


class ChainResDto(BaseModel):
    header: Block.Header
    body: Block.Body
