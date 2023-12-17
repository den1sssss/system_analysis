from task import task


def exec_task(funct):
    try:
        return [0, funct]
    except ValueError:
        return [1]


def check_value(val, ref):
    return val == ref


def check_task(res, ref):
    if res[0] == 0:
        if check_value(res[1], ref):
            return '11'
        else:
            return '01'
    else:
        return '00'


# Порядок значений: H(AB), H(A), H(B), Ha(B), Ia,b
reference = [4.34, 3.27, 4.04, 1.06, 2.98]
result = exec_task(task())
print(check_task(result, reference))