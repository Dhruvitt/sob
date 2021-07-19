# sob-prototype
This is submission prototype for Summer of Bitcoin
 A program which reads a file mempool.csv, with the format:
  <txid>,<fee>,<weight>,<parent_txids>
  txid is the transaction identifier
  fee is the transaction fee
  weight is the transaction weight
  parent_txids is a list of the txids of the transaction’s unconfirmed parent transactions (confirmed parent transactions are not included in this list). It is of
  the form: <txid1>;<txid2>;...
  
The output from the program is txids, separated by newlines, which make a valid block, maximizing the fee to the miner. Transactions MUST appear in order
(no transaction should appear before one of its parents).
