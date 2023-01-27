# Async Functions

## Introductions
The asyncio pakage contains all the tools that will be used to produce a asynchronous function
```python
import asyncio

async def send_email():
	print("Used in a real Applications")

asyncio.run(send_email())
```
An asynchorous function in python is normall called a coroutine. Coroutine are decalred with the async/await syntax. Coroutine are special functions that return coroutine objects when called.

## Explanation of sub functions in the async package.
1. **async.run** - This function is used to run a python coroutine. It does not return anything unless the function tell it to return a value or something else.
2. **async.iscoroutinefunction** - This function is meant to verify whether a function us a coroutine function. It returns true f it is and returns false if it is not.
3. **await** - The await command preceeds or starts a task that potentially may take a couple of seconds to complete ot time to complete. When it does complete, the result of the task can then be returned and the other parts of the code can continue.
4. **asyncio.sleep** - This function is going to provide a way of simulating some sort of delay so that some action can be preformed and some features can be show cased. 
5. **asyncio.create_task** - This function is meant to be used to create tasks in an asynchronous programming paradigm. It can be used to initialized to an asynchoronous function.

## Event Loop
The Event loop is a very efficient task manager. It coordinates tasks. It also runs asynchrinius tasks and callback. 