import asyncio
from web3 import AsyncWeb3, AsyncHTTPProvider


addresses = [
    "0xdadB0d80178819F2319190D340ce9A924f783711",
    "0x8860Be55F15dd189BEd1c3B5A797DC8CD60f2121",
    "0x95222290DD7278Aa3Ddd389Cc1E1d165CC4BAfe5"
]

async def get_balance(w3_async):
    for address in addresses:
        checksum_address = w3_async.to_checksum_address(address)
        balance = await w3_async.eth.get_balance(checksum_address)
        ether_balance = w3_async.from_wei(balance, 'ether')
        print(f"Адрес: {checksum_address}, баланс: {ether_balance}")

async def main():
    w3_async = AsyncWeb3(AsyncHTTPProvider('https://rpc.ankr.com/eth'))
    await get_balance(w3_async)


asyncio.run(main())