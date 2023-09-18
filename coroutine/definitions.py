import asyncio


# define a coroutine
async def custom_coro():
    await asyncio.sleep(1)


async def main():
    await custom_coro()

# create the coroutine
coro = custom_coro()
# check the type of the coroutine
print(type(coro))

asyncio.run(main())
