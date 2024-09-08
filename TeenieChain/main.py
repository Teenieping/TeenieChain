import uvicorn
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from TeenieChain import TeenieChain
app = FastAPI()
teenieChain = TeenieChain()


@app.get('/mint')
async def mint(request):
    pass


@app.get('/proof_of_work')
async def proof_of_work(request):
    pass


@app.get('/hash')
async def hash(request):
    pass


@app.get('/name')
async def name():
    return JSONResponse({
        "name": f"{teenieChain.name()}"
    })


@app.get('/chain')
async def chain():
    print(teenieChain.chain)
    return teenieChain.chain


@app.get('/get-previous-block')
async def get_previous_block():
    return teenieChain.get_previous_block()


@app.get('/get-previous-proof')
async def get_previous_proof():
    return JSONResponse({
        "proof": f"{teenieChain.get_previous_proof()}"
    })


@app.get('/get-chain')
async def get_chain():
    return JSONResponse({
        "chain": f"{teenieChain.get_chain()}"
    })


@app.get('/total-supply')
async def get_total_supply():
    return JSONResponse({
        "supply": f"{teenieChain.total_supply()}"
    })

if __name__ == '__main__':
    uvicorn.run("main:app", host="0.0.0.0", port=8000)
