from fastapi import APIRouter, Depends

from api.src.domain.chain.dto.req.BlockReqDto import BlockReqDto
from api.src.domain.chain.dto.req.MintReqDto import MintReqDto
from api.src.domain.chain.dto.req.PowReqDto import PowReqDto
from api.src.domain.chain.service.ChainService import ChainService

ChainRouter = APIRouter()


@ChainRouter.post('/mint')
async def mint(dto: MintReqDto, chainService: ChainService = Depends(ChainService)):
    return chainService.mint(dto)


@ChainRouter.post('/proof_of_work')
async def proof_of_work(dto: PowReqDto, chainService: ChainService = Depends(ChainService)):
    return chainService.pow(dto)


@ChainRouter.get('/hash')
async def hash(dto: BlockReqDto, chainService: ChainService = Depends(ChainService)):
    return chainService.hash(dto)


@ChainRouter.get('/name')
async def name(chainService: ChainService = Depends(ChainService)):
    return chainService.get_chain_name()


@ChainRouter.get('/chain')
async def chain(chainService: ChainService = Depends(ChainService)):
    return chainService.get_chain()


@ChainRouter.get('/get-previous-block')
async def get_previous_block(chainService: ChainService = Depends(ChainService)):
    return chainService.get_previous_block()


@ChainRouter.get('/get-previous-proof')
async def get_previous_proof(chainService: ChainService = Depends(ChainService)):
    return chainService.get_previous_block()


@ChainRouter.get('/total-supply')
async def get_total_supply(chainService: ChainService = Depends(ChainService)):
    return chainService.get_total_supply()
