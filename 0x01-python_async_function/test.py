import asyncio

async def send_email():
	print("I am going to sleep")
	await asyncio.sleep(10)
	print("I have slept. I am now awake.")

async def t1():
	await t2()
	print("t1")
async def t2():
	await t3()
	print("t2")
async def t3():
	print("t3")
# print(asyncio.iscoroutinefunction(send_email))


async def file_reply():
	await asyncio.sleep(4)
	return {"File Returned"}

async def data_reply():
	await asyncio.sleep(9)
	return {"data":100}


async def task1():
	print("Waiting for data...")
	x = await data_reply()
	print(x)
	return "Task 1 Done"


async def task2():
	print("Waiting for file...")
	x = await file_reply()
	print(x)
	return "Task 2 Done"

async def main():
	x = asyncio.create_task(task1())
	y = asyncio.create_task(task2())

	await x
	await y
	return "Testing Async Package"

async def a1():
	x = asyncio.create_task(a2())
	await x
	print("a3.get_name()")
async def a2():
	x = asyncio.create_task(a3())
	await x
	print("a2.get_name()")
async def a3():
	x = asyncio.create_task(a1())
	await x
	print("a1.get_name()")

# print(asyncio.run(a1()))

# Secrion that builds a coroutine called fetch data
async def fetch_data():
	print("Fetching data...")
	await asyncio.sleep(6)
	print("Data returned...")
	return {"data": 100}

async def count_down():
	for i in range(10, 1, -1):
		print(i)
		await asyncio.sleep(2)

async def main():
	x = asyncio.create_task(fetch_data())
	y = asyncio.create_task(count_down())
	data = await x
	print(data)
	await y
asyncio.run(main())

