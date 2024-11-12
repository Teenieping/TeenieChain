from pathlib import Path

import uvicorn
from fastapi import FastAPI
from TeenieChain.TeenieChain import TeenieChain
from api.src.domain.chain.controller.ChainController import ChainRouter

BASE_DIR = Path(__file__).resolve().parent.parent
app = FastAPI()
app.include_router(ChainRouter)
teenieChain: TeenieChain = TeenieChain()


if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)
