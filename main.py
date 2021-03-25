from utils import timing
import numpy as np
import concurrent.futures
import time


parallel_code_time = 0
sequential_code_time = 0


@timing
def bubble(array):
    for i in range(len(array) - 1):
        for j in range(len(array) - i - 1):
            if array[j] > array[j + 1]:
                buff = array[j]
                array[j] = array[j + 1]
                array[j + 1] = buff
    return array


@timing
def matmul(cortege_matrix_size):
    matrixA = list(np.random.randint(-1000, 1000, cortege_matrix_size))
    matrixB = list(np.random.randint(-1000, 1000, cortege_matrix_size))

    return [[sum(x * y for x, y in zip(m1_r, m2_c)) for m2_c in zip(*matrixB)] for m1_r in matrixA]


@timing
def matrix_task(cortege_matrix_size):

    composition = cortege_matrix_size[0] * cortege_matrix_size[1]
    matrixA = np.arange(0, composition).reshape(cortege_matrix_size)
    matrixB = np.arange(0, composition).reshape(cortege_matrix_size)
    result = np.dot(matrixA, matrixB)


def threads(k, workers):
    tasks = [(k, k) for _ in range(8)]
    # tasks = [[random.randint(-1000, 1000) for _ in range(k)] for s in range(8)]

    with concurrent.futures.ProcessPoolExecutor(max_workers=workers) as executor:
        start = time.time()
        for _ in executor.map(matmul, tasks):
            ...
        end = time.time()
        global parallel_code_time
        parallel_code_time = end-start


if __name__ == '__main__':
    time_start_full = time.time()
    threads(k=200, workers=8)
    time_end_full = time.time()
    sequential_code_time = time_end_full-time_start_full
    print(f"Общее время выполнения  функций - {sequential_code_time} секунд.")
    print(f"Общее время выполнения распалелеленых функций - {parallel_code_time:.4f} секунд.")
    print(f"Время выполнения последовательных функций - {sequential_code_time-parallel_code_time:.4f} секунд.")
    print(f"Доля распаралеленного кода - {(parallel_code_time/sequential_code_time):.4f} %")
    print(f"Доля паралельного кода - {1-(parallel_code_time / sequential_code_time):.4f} %")
