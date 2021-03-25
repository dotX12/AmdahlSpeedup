# func: matmul Время выполнения - 1.497 сек.
# func: matmul Время выполнения - 1.5509 сек.
# func: matmul Время выполнения - 1.5319 сек.
# func: matmul Время выполнения - 1.523 сек.
# func: matmul Время выполнения - 1.5529 сек.
# func: matmul Время выполнения - 1.6058 сек.
# func: matmul Время выполнения - 1.5031 сек.
# func: matmul Время выполнения - 1.5567 сек.
# Общее время выполнения  функций - 13.056562185287476 секунд.
# Общее время выполнения распалелеленых функций - 13.0241 секунд.
# Время выполнения последовательных функций - 0.0325 секунд.
# Доля распаралеленного кода - 0.9975 %
# Доля паралельного кода - 0.0025 %

parallel = 0.0024
time = 13.056562185287476
for i in range(2, 9):
    b = ((1 + (1 - parallel)) / i)
    sp = 1 / b
    print(f"Количество ядер: {i}. Прирост : {sp:.4f} Время выполнения : {time / sp:.4f}")
