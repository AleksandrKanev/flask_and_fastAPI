import time
import random
import asyncio

arr = [random.randint(1, 100) for _ in range(1_000_000)]
COUNT = 1000
counter = 0
sum_ = 0


async def sum_num_thr(count):
    global sum_
    for i in range(count, count + COUNT):
        sum_ += arr[i]


async def main():
    global counter
    tasks = []
    for _ in range(int(1_000_000 / COUNT)):
        t = asyncio.create_task(sum_num_thr(counter))
        tasks.append(t)
        counter += COUNT
    await asyncio.gather(*tasks)


if __name__ == '__main__':
    start_time = time.time()
    asyncio.run(main())
    print(time.time() - start_time)
