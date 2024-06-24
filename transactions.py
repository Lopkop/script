from solathon.core.instructions import transfer
from solathon import Client, Transaction, PublicKey, Keypair


def make_transactions(private_key: str):
    client = Client("https://api.devnet.solana.com")

    sender = Keypair.from_private_key(private_key)
    receiver1 = PublicKey("4RCWU6r7oFaKKt5BbAWisiBsBscRpL2hDqv89Ric9v2r")
    receiver2 = PublicKey("GUh1KwvgX5b2QFBG46KsCw43T3TRHZwer2oTRCPHRz8S")
    receiver3 = PublicKey("98njFGB6xQ3TCv7FR7UhkNRiR2xuGwFYnPv6Gqy7kpXn")
    amount = 0.1  # solana

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
