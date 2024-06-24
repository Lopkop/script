import os
from dotenv import load_dotenv

from transactions import make_transactions
from market import load_phantom, load_raydium

load_dotenv()

PRIVATE_KEY = os.getenv("PRIVATE_KEY")

if __name__ == '__main__':
    make_transactions(PRIVATE_KEY)
    load_phantom(PRIVATE_KEY)
    load_raydium()
