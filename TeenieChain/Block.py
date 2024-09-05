from datetime import datetime
from typing import List

from transactions import Transaction


class Block:
    def __init__(
            self,
            version: str,
            previous_hash: int,
            proof: int,
            merkle_root: hex,
            timestamp: datetime,
            aim_level: hex,
            nonce: int = None,
            transaction: Transaction = None,
    ):
        self.Header.version = version
        self.Header.previous_hash = previous_hash
        self.Header.proof = proof or 0
        self.Header.merkle_root = merkle_root
        self.Header.timestamp = timestamp
        self.Header.aim_level = aim_level
        self.Header.nonce = nonce or 0

        self.Body.transaction = transaction

    class Header:
        version: str
        previous_hash: int
        proof: int
        merkle_root: hex
        timestamp: datetime
        aim_level: hex
        nonce: int

    class Body:
        transaction: List[Transaction]

    @staticmethod
    def serialize(block):
        return {
            "header": {
                "version": block.Header.version,
                "previous_hash": block.Header.previous_hash,
                "proof": block.Header.proof,
                "merkle_root": block.Header.merkle_root,
                "timestamp": str(block.Header.timestamp.isoformat()),
                "aim_level": block.Header.aim_level,
                "nonce": block.Header.nonce
            },
            "body": {
                "transaction": block.Body.transaction if block.Body.transaction else []
            }
        }
