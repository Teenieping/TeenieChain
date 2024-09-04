from datetime import datetime


class Transaction:
    sender: str
    recipient: str
    amount: int
    timestamp: datetime

    def __init__(
            self,
            sender: str,
            recipient: str,
            amount: int
    ):
        self.sender = sender
        self.recipient = recipient
        self.amount = amount
        self.timestamp = datetime.now()

    def __repr__(self) -> str:
        return (
            f"Transaction(\n"
            f"  sender={self.sender}\n"
            f"  recipient={self.recipient}\n"
            f"  amount={self.amount}\n"
            f"  timestamp={self.timestamp}\n"
            f")"
        )
