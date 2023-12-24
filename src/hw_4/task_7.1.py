# Напишите программу на Python, которая будет находить
# сумму элементов массива из 1000000 целых чисел.
# � Пример массива: arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, ...]
# � Массив должен быть заполнен случайными целыми числами
# от 1 до 100.
# � При решении задачи нужно использовать многопоточность,
# многопроцессорность и асинхронность.
# � В каждом решении нужно вывести время выполнения
# вычислений.

import time
import random
import threading

arr = [random.randint(1, 100) for _ in range(1_000_000)]
COUNT = 1000
counter = 0
sum_ = 0


def sum_num_thr(count):
    global sum_
    for i in range(count, count + COUNT):
        sum_ += arr[i]


def threads_():
    global counter
    threads = []
    for _ in range(int(1_000_000 / COUNT)):
        t = threading.Thread(target=sum_num_thr, args=(counter,))
        threads.append(t)
        t.start()
        counter += COUNT

    for t in threads:
        t.join()


if __name__ == '__main__':
    start_time = time.time()
    threads_()
    print(f'threads_ = {time.time() - start_time}')
