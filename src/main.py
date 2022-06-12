class Blockchain():
    def __init__():
        self.chain = []
        self.current_transactions = []

    def new_block(self):
        # Creates a new Block into the chain
        pass

    def new_transaction(self, sender:str, recipient:str, amount: int) -> int:
        """
        Creates a new transaction to go into the mined Block
        :param sender: <str> Address of the Sender
        :param recipient: <str> Address of the Recipient
        :param amount: <int> Amount 
        """

        self.current_transactions.append({
            'sender': sender,
            'recipient': recipient,
            'amount': amount,
        })

        return self.last_block['index'] + 1

    @staticmethod
    def hash(block):
        # Hashes a block
        pass

    @property
    def last_block(self):
        # Returns the last block in the chain
        pass

