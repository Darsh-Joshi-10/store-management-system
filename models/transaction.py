from datetime import datetime

class Transaction:
    #Represents an audit trail log entry for stock changes.
    VALID_TYPES = ("RESTOCK", "SALE", "ADJUSTMENT")

    def __init__(self, product_id : int, transaction_type : str, quantity:int, transaction_id : int | None = None, timestamp : str|None = None):
        if transaction_type.upper() not in self.VALID_TYPES:
            raise ValueError("Invalid transaction type")

        self.transaction_id = transaction_id
        self.product_id = product_id
        self.transaction_type = transaction_type.upper()
        self.quantity = quantity
        self.timestamp = timestamp or datetime.now().strftime("%Y- %m-%d %H:%M:%S")

    def __repr__(self)->str:
        return f"<Transaction(id={self.transaction_id}, product_id={self.product_id}, type='{self.transaction_type}', qty={self.quantity})>"
