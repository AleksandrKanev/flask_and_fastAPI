import time
import random
import multiprocessing

COUNT = 1000
sum_ = multiprocessing.Value('i', 0)


def sum_num_thr(cnt, arr):
    with cnt.get_lock():
        for i in arr:
            cnt.value += i


def multiprocess():
    arr = [random.randint(1, 100) for _ in range(1_000_000)]
    print(sum(arr))
    counter_ = 0
    multiprocess_ = []
    for _ in range(int(1_000_000 / COUNT)):
        new_arr = []
        for i in range(counter_, counter_ + 1000):
            new_arr.append(arr[i])
        p = multiprocessing.Process(target=sum_num_thr, args=(sum_, new_arr))
        multiprocess_.append(p)
        p.start()
        counter_ = counter_ + COUNT

    for p in multiprocess_:
        p.join()


if __name__ == '__main__':
    start_time = time.time()
    multiprocess()
    print(f'multiprocess = {time.time() - start_time}')
