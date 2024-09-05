import hashlib
import json
from datetime import datetime
from typing import List

from Block import Block


class TeenieChain:
    # Todo chain
    chain: List[Block]
    end_TIE_of_limit: float
    CHAIN_LIMIT: int = 30000

    def __init__(self):
        self.chain = []
        self.mint(previous_hash=0x0, proof=0x0)

    """
        mint - Create New Block
        
        Create Block with mining
        
        previous_block = teenieChain.get_previous_block()
        previous_proof = previous_block["header"]["proof"]
        new_proof = teenieChain.mining(previous_proof=previous_proof)
        previous_hash = teenieChain.hash(previous_block)
        if teenieChain.proof_of_work(previous_proof=previous_proof, new_proof=new_proof):
            teenieChain.mint(proof=new_proof, previous_hash=previous_hash)
            print(len(teenieChain.chain), teenieChain.chain[i]["header"], teenieChain.end_TIE_of_limit)
    """

    def mint(
            self,
            previous_hash: hex,
            proof: int
    ) -> Block | str:
        if self.chain_available() is False:
            return "Chain Limit!"

        _new_block = Block(
            version="0.1.0",
            previous_hash=previous_hash,
            proof=proof,
            merkle_root="0",  # Todo
            timestamp=datetime.now(),
        )

        self.chain.append(Block.serialize(_new_block))
        self.end_TIE_of_limit = len(self.chain)/self.CHAIN_LIMIT * 100  # Update 
        return _new_block

    def get_previous_block(self) -> Block:
        return self.chain[-1]

    @staticmethod
    def mining(previous_proof: hex) -> int:
        new_proof = 0x1
        check_proof = False

        while not check_proof:
            operation = hashlib.sha256(str(new_proof ** 2 - previous_proof ** 2).encode()).hexdigest()
            if operation.startswith("00000"):
                check_proof = True
            else:
                new_proof += 1
        return new_proof

    @staticmethod
    def proof_of_work(previous_proof, new_proof) -> bool:
        operation = hashlib.sha256(str(new_proof ** 2 - previous_proof ** 2).encode()).hexdigest()
        if operation.startswith("0000"):
            return new_proof
        return False

    def hash(self, block: Block) -> str:
        encoded_block = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(encoded_block).hexdigest()

    def chain_available(self) -> bool:
        if len(self.chain) >= self.CHAIN_LIMIT:
            return False

        return True

