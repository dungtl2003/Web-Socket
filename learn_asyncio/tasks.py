import asyncio
import time
from learn_asyncio.utils import (
    say_after,
)


async def main():
    task1 = asyncio.create_task(
        say_after(1, 'hello')
    )

    task2 = asyncio.create_task(
        say_after(0, 'world')
    )

    print(f"Start at {time.strftime('%X')}")

    await task1

    print(f"Finish at {time.strftime('%X')}")


asyncio.run(main())
