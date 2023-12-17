import json
import numpy as np

def calc_list_of_ranks(r_str: str, tmpl: dict) -> list[int]:
    r = json.loads(r_str)
    r_list = [0] * len(tmpl)

    for i, el in enumerate(r):
        if isinstance(el, list):
            for sub_el in el:
                r_list[tmpl[sub_el]] = i + 1
        else:
            r_list[tmpl[el]] = i + 1

    return r_list

def create_ranking_template(template_str: str) -> dict:
    template = dict()
    count = 0

    for element in json.loads(template_str):
        if isinstance(element, list):
            for sub_element in element:
                template[sub_element] = count
                count += 1
        else:
            template[element] = count
            count += 1

    return template

def calculate_D_Dmax(matrix: np.ndarray) -> float:
    sum_matrix = np.sum(matrix, axis=0)
    D = np.var(sum_matrix) * matrix.shape[0] / (matrix.shape[0] - 1)
    D_max = (matrix.shape[1] ** 2) * ((matrix.shape[0] ** 3 - matrix.shape[0]) / 12) / (matrix.shape[0] - 1)
    
    return D / D_max

def task(*rankings) -> str:
    experts_count = len(rankings)
    template = create_ranking_template(rankings[0])
    matrix = np.array([calc_list_of_ranks(r_str, template) for r_str in rankings])
    
    result = calculate_D_Dmax(matrix)
    
    return format(result, ".2f")

if __name__ == "__main__":
    A = '["1", ["2", "3"], "4", ["5", "6", "7"], "8", "9", "10"]'
    B = '[["1", "2"], ["3", "4", "5"], "6", "7", "9", ["8", "10"]]'
    C = '["3", ["1", "4"], "2", "6", ["5", "7", "8"], ["9", "10"]]'

    print(task(A, B, C))
