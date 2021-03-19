import hashlib


class Block:
    def _init_(self, previous_hash, transaction):
        self.transactions = transaction
        self.previous_hash = previous_hash
        string_to_hash = "".join(transaction) + previous_hash
        self.block_hash = hashlib.sha256(string_to_hash.encode()).hexdigest()
