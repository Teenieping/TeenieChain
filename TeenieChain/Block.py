from datetime import datetime
from typing import List

from transactions import Transaction


class Block:
    def __init__(
            self,
            version: str,
            previous_hash: str,
            merkle_root: str,
            timestamp: datetime,
            aim_level: int,
            nonce: int,

            transaction: Transaction,
    ):
        self.Header.version = version
        self.Header.previous_hash = previous_hash
        self.Header.merkle_root = merkle_root
        self.Header.timestamp = timestamp
        self.Header.aim_level = aim_level
        self.Header.nonce = nonce

        self.Body.transaction = transaction

    class Header:
        version: str
        previous_hash: str
        merkle_root: str
        timestamp: datetime
        aim_level: int
        nonce: int

    class Body:
        transaction: List[Transaction]
