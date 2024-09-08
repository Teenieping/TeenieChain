import hashlib
import json
from datetime import datetime
from typing import List

from Block import Block


class TeenieChain:
    # Todo chain
    chain: List
    end_TIE_of_limit: float
    AIM_LEVEL: hex  = 0x0000FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF
    MERKEL_ROOT     = 000000000000000000000000000000000000000000000000000000000000000000

    def __init__(self):
        self.chain = []
        self.mint(previous_hash=0x0, proof=0x0)
        # Todo Transaction

    """
        mint - Create New Block
        
        hashlib.sha256(str(new_proof ** 2 - previous_proof ** 2).encode()).hexdigest()
        
        Create Block with mining
    """

    def mint(
            self,
            previous_hash: int,
            proof: int,
            # Todo Transaction
    ):

        _new_block = Block(
            version="0.1.0",
            previous_hash=previous_hash,
            proof=proof,
            merkle_root=TeenieChain.MERKEL_ROOT,
            aim_level=self.AIM_LEVEL,
            timestamp=datetime.now(),
            nonce=proof,
        )

        c = self.chain.append(Block.serialize(_new_block))
        del _new_block
        return c

    def mining(self, previous_proof: int) -> int:
        new_proof = 0x1
        check_proof = False

        while not check_proof:
            operation = hashlib.sha256(str(new_proof ** 2 - previous_proof ** 2).encode()).hexdigest()
            print(operation)
            if int(operation, 16) < self.AIM_LEVEL:
                check_proof = True
            else:
                new_proof += 1
        return new_proof

    def proof_of_work(self, previous_proof, new_proof) -> bool:
        operation = hashlib.sha256(str(new_proof ** 2 - previous_proof ** 2).encode()).hexdigest()
        return int(operation, 16) < self.AIM_LEVEL

    def hash(self, block: Block) -> str:
        encoded_block = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(encoded_block).hexdigest()

    """
        TeenieChain TNE20
    """ 
    @staticmethod
    def name() -> str:
        return "TeenieChain"

    def get_previous_block(self) -> Block:
        return self.chain[-1]

    def get_previous_proof(self) -> int:
        return self.chain[-1]["header"]["proof"]

    def get_chain(self) -> list[Block]:
        return self.chain

    def total_supply(self) -> int:
        return len(self.chain)


"""

test

if __name__ == "__main__":
    teenieChain = TeenieChain()

    for i in range(10):
        previous_proof = teenieChain.get_previous_proof()
        new_proof = teenieChain.mining(previous_proof=previous_proof)
        previous_hash = teenieChain.hash(teenieChain.get_previous_block())
        if teenieChain.proof_of_work(previous_proof=previous_proof, new_proof=new_proof):
            teenieChain.mint(proof=new_proof, previous_hash=int(previous_hash, 16))
"""
