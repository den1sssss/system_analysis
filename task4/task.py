import numpy as np

def calculate_entropy(probabilities):
    return -np.sum(probabilities * np.log2(probabilities, where=np.abs(probabilities) > 1e-4))

def task():
    sum_values = sorted({side1 + side2 for side1 in range(1, 7) for side2 in range(1, 7)})
    proizv_values = sorted({side1 * side2 for side1 in range(1, 7) for side2 in range(1, 7)})

    sL = {item: index for index, item in enumerate(sum_values)}
    pL = {item: index for index, item in enumerate(proizv_values)}

    combinations = np.zeros((len(sum_values), len(proizv_values)))
    for side1 in range(1, 7):
        for side2 in range(1, 7):
            combinations[sL[side1 + side2], pL[side1 * side2]] += 1

    combinProbabilities = combinations / 36
    
    cp_A = np.sum(combinProbabilities, axis=1)
    cp_B = np.sum(combinProbabilities, axis=0)

    H_AB = calculate_entropy(combinProbabilities)
    H_A = calculate_entropy(cp_A)
    H_B = calculate_entropy(cp_B)
    Ha_B = H_AB - H_A
    I_AB = H_B - Ha_B

    result = [round(item, 2) for item in [H_AB, H_A, H_B, Ha_B, I_AB]]
    return result

if __name__ == "__main__":
    print(task())
