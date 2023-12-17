import numpy as np
import json

def flatten_list(lst):
    return [item for sublist in lst for item in sublist]

def build_adjacency_matrix(line):
    line = json.loads(line)
    used = set()
    matrix_size = len(flatten_list(line))
    result_matrix = np.zeros((matrix_size, matrix_size))

    for elx in line:
        for x in elx:
            for ely in line:
                for y in ely:
                    if y not in used:
                        result_matrix[int(x) - 1][int(y) - 1] = 1
        used.update(elx)

    return result_matrix

def compare_matrices(matrix1, matrix2):
    result_matrix = np.ones((len(matrix1[0]), len(matrix1[0])))

    for i in range(len(matrix1[0]) - 1):
        if matrix1[i + 1][i] != matrix2[i + 1][i] and matrix1[i][i + 1] != matrix2[i][i + 1]:
            result_matrix[i + 1][i] = 0
            result_matrix[i][i + 1] = 0

    return result_matrix

def result(result_matrix):
    ind_list = []
    i = 0

    while i < len(result_matrix[0]):
        if result_matrix[i][i - 1] == 0:
            ind_list.pop()
            ind_list.append([str(i), str(i + 1)])
        else:
            ind_list.append(str(i + 1))
        i += 1

    return json.dumps(ind_list)

def task(line1, line2):
    matrix1 = build_adjacency_matrix(line1)
    matrix2 = build_adjacency_matrix(line2)
    result_matrix = compare_matrices(matrix1, matrix2)
    return result(result_matrix)

if __name__ == "__main__":
    print(task('[["1","2"],["3","4","5"],"6","7","9",["8","10"]]','["1",["2","3"],"4",["5","6","7"],"8","9","10"]'))
