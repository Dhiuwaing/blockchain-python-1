# consist blocks
# blocks consist transactions
# blocks are connected through hashing
# unique digital fingerprint - transation + previous blocks fingerprint

from Block import Block


blockchain = []
genesis_block = Block("Chancellor on the brink...", ["Satoshi sent 1 BTC to Ivan",
                                                     "Maria sent 5 BTC to Jenny",
                                                     "Satoshi sent 5 BTC to Hal Finney"])

print(genesis_block.block_hash)
