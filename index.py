from  main import Block

blockchain = []

genesis_block = Block("This is Ashish...",["raj sent 3 BTC to Sham", 
                                          "king sent 2 BTC to Slave ",
                                           "Sam sent 5 BTC to Olive" ])

second_block = Block(genesis_block.block_hash,["X 5 BTC to Z","A 4 BTC to B"])

third_block = Block(second_block.block_hash,["X 5 BTC to Z","A 5 BTC to B"])

#print(genesis_block.block_hash)
print(second_block.block_hash)
#print(third_block.block_hash)