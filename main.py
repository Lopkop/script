import os
from dotenv import load_dotenv

from transactions import make_transactions
from market import load_phantom, create_market

load_dotenv()

PRIVATE_KEY = os.getenv("PRIVATE_KEY")
PUBLIC_KEY1 = os.getenv("PUBLIC_KEY1")
PUBLIC_KEY2 = os.getenv("PUBLIC_KEY2")
PUBLIC_KEY3 = os.getenv("PUBLIC_KEY3")
BASE_COIN = os.getenv("BASE_COIN")
QUOTE_TOKEN = os.getenv("QUOTE_TOKEN")

if __name__ == '__main__':
    # make_transactions(PRIVATE_KEY, PUBLIC_KEY1, PUBLIC_KEY2, PUBLIC_KEY3)
    load_phantom(PRIVATE_KEY)
    create_market(BASE_COIN, QUOTE_TOKEN)
    # create_liquidity_pool()
    # run_swap()
