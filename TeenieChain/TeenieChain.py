from datetime import datetime
from typing import List

from block import Block
from transactions.Transaction import Transaction


class TeenieChain:
    # Todo chain
    chain: List[Block] = []

    def __init__(self):
        pass

    """
        mint - Create New Block
    """
    @staticmethod
    def mint(
            previous_hash: str,
            aim_level: int,
            nonce: int,
            sender: str,
            recipient: str,
            amount: int
    ) -> Block:
        """Initialize new Block"""
        _new_block = Block(
            version="0.1.0",
            previous_hash=previous_hash,
            merkle_root="0",
            timestamp=datetime.now(),
            aim_level=aim_level,
            nonce=nonce,
            transaction=Transaction(
                sender=sender,
                recipient=recipient,
                amount=amount
            )
        )
        return _new_block

    """
        verify_hash - Verify hash and append at chain
    """
    def verify_hash(self, block: Block):
        # Todo verify hash logic

        self.chain.append(block)
        return block


if __name__ == "__main__":
    block = TeenieChain.mint(
        previous_hash="0",
        aim_level=1,
        nonce=1,
        sender="0",
        recipient="0",
        amount=100
    )
    print(block.Body.transaction)
    print(TeenieChain.chain)
