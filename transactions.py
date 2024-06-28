from solathon.core.instructions import transfer
from solathon import Client, Transaction, PublicKey, Keypair


def make_transactions(private_key: str, pbk1: str, pbk2: str, pbk3: str):
    client = Client("https://api.mainnet-beta.solana.com")

    sender = Keypair.from_private_key(private_key)
    receiver1 = PublicKey(pbk1)
    receiver2 = PublicKey(pbk2)
    receiver3 = PublicKey(pbk3)
    amount = 0.1  # solana
    print('ALO')
    instruction1 = transfer(
        from_public_key=sender.public_key,
        to_public_key=receiver1,
        lamports=int(amount * 10 ** 9)
    )
    instruction2 = transfer(
        from_public_key=sender.public_key,
        to_public_key=receiver2,
        lamports=int(amount * 10 ** 9)
    )
    instruction3 = transfer(
        from_public_key=sender.public_key,
        to_public_key=receiver3,
        lamports=int(amount * 10 ** 9)
    )
    transaction = Transaction(instructions=[instruction1, instruction2, instruction3], signers=[sender])
    result = client.send_transaction(transaction)

    print("Transaction response:", result)
