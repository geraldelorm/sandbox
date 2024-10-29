import asyncio

async def process_transaction(transaction):
    await asyncio.sleep(1)  # Simulate a network call or computation
    return transaction * 1.02  # Example processing

async def main(transactions):
    processed_transactions = await asyncio.gather(
        *[process_transaction(t) for t in transactions]
    )
    print("Processed transactions:", processed_transactions)

transactions = [100, 200, 300]
asyncio.run(main(transactions))