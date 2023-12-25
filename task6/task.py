import json
import numpy as np

def task(first_order, second_order, third_order):
    first_order = json.loads(first_order)
    second_order = json.loads(second_order)
    third_order = json.loads(third_order)

    n = len(first_order)
    res = np.zeros(n)
    avg = np.sum([int(first_order[i][1]) + int(second_order[i][1]) + int(third_order[i][1]) for i in range(n)]) / n

    desp = np.sum([(el - avg) ** 2 for el in res]) / (2 * 9 * (n ** 3 - n) / (12 * (n - 1)))

    return desp

if __name__ == "__main__":
    print(task(
        '["O1","O2","O3"]',
        '["O1","O3","O2"]',
        '["O1","O3","O2"]'))

