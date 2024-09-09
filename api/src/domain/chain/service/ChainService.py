from typing import List
from fastapi.exceptions import HTTPException

from TeenieChain.Block import Block
from api.src.domain.chain.dto.req.BlockReqDto import BlockReqDto
from api.src.domain.chain.dto.req.MintReqDto import MintReqDto
from api.src.domain.chain.dto.req.PowReqDto import PowReqDto
from api.src.domain.chain.dto.res.HashResDto import HashResDto


class ChainService:

    @staticmethod
    def mint(dto: MintReqDto):
        from api.main import teenieChain
        mint = teenieChain.mint(
            previous_hash=dto.previous_hash,
            proof=dto.proof,
            # Todo transaction
        )
        return mint

    @staticmethod
    def hash(dto: BlockReqDto):
        from api.main import teenieChain
        hash = teenieChain.hash(block=dto.block)
        return HashResDto(
            hash=hash
        )

    @staticmethod
    def pow(dto: PowReqDto):
        from api.main import teenieChain
        pow = teenieChain.proof_of_work(
            previous_proof=dto.previous_proof,
            new_proof=dto.proof,
        )
        if pow is False:
            raise HTTPException(400, 'POW is not valid.')

    @staticmethod
    def get_chain_name():
        from api.main import teenieChain
        return teenieChain.name()

    @staticmethod
    def get_chain() -> List[Block]:
        from api.main import teenieChain
        return teenieChain.chain

    @staticmethod
    def get_previous_block():
        from api.main import teenieChain
        return teenieChain.get_previous_block()

    @staticmethod
    def get_total_supply():
        from api.main import teenieChain
        return teenieChain.total_supply()
