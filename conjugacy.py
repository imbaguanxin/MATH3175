import re


def cal_perm(a, b):
    result = {}
    for i in range(len(a)):
        k = i + 1
        result[k] = a[b[k]]
    return result


def from_cycle(length, cyc):
    result = {}
    for i in range(length):
        result[i + 1] = i + 1

    for i in range(len(cyc) - 1):
        curr = cyc[i]
        nxt = cyc[i + 1]
        result[curr] = nxt
    result[cyc[-1]] = cyc[0]
    return result


def from_cycles(length, cycs):
    result = {}
    for i in range(length):
        result[i + 1] = i + 1
    for cyc in cycs:
        cyc_dic = from_cycle(length, cyc)
        result = cal_perm(result, cyc_dic)
    return result


def to_cycle(length, str):
    result = {}
    for i in range(length):
        result[i + 1] = i + 1
    pattern = re.compile(r"\(\d+\b\)")
    cycs = pattern.findall(str)
    # print(cycs)
    cycs_list = []
    for cyc in cycs:
        pattern = re.compile("\d+")
        cyc_str = pattern.findall(cyc)[0]
        # print(cyc_str)
        cyc_list = [None] * len(cyc_str)
        for i in range(len(cyc_list)):
            cyc_list[i] = int(cyc_str[i])
        # print(cyc_list)
        cycs_list.append(cyc_list)
    result = cal_perm(result, from_cycles(length, cycs_list))
    return result


def perm_to_str(perm):
    result = ""
    while perm:
        key = perm[list(perm.keys())[0]]
        if not key == perm[key]:
            result = result + "("
            start = key
            end = perm[key]
            while not key == end:
                result = result + str(start)
                del perm[start]
                start = end
                end = perm[end]
            result = result + str(start)
            del perm[start]
            result = result + ")"
        else:
            del perm[key]
    if result == "":
        return "(1)"
    return result


if __name__ == '__main__':
    a = {1: 3, 2: 2, 3: 4, 4: 1, 5: 5}
    b = {1: 2, 2: 3, 3: 1, 4: 4, 5: 5}
    # result = cal_perm(b, a)
    # p = from_cycle(5, [[1, 3, 4]])
    result1 = perm_to_str(to_cycle(5, "(123)(134)(321)"))
    result2 = perm_to_str(to_cycle(5, "(123)(143)(321)"))
    print([result1, result2])

    result1 = perm_to_str(to_cycle(5, "(132)(134)(231)"))
    result2 = perm_to_str(to_cycle(5, "(132)(143)(231)"))
    print([result1, result2])
    print(perm_to_str(to_cycle(5, "(432)(342)")))

    result1 = perm_to_str(to_cycle(5, "(124)(134)(421)"))
    result2 = perm_to_str(to_cycle(5, "(124)(143)(421)"))
    print([result1, result2])

    result1 = perm_to_str(to_cycle(5, "(142)(134)(241)"))
    result2 = perm_to_str(to_cycle(5, "(142)(143)(241)"))
    print([result1, result2])

    result1 = perm_to_str(to_cycle(5, "(125)(134)(521)"))
    result2 = perm_to_str(to_cycle(5, "(125)(143)(521)"))
    print([result1, result2])

    result1 = perm_to_str(to_cycle(5, "(152)(134)(251)"))
    result2 = perm_to_str(to_cycle(5, "(152)(143)(251)"))
    print([result1, result2])

    result1 = perm_to_str(to_cycle(5, "(134)(134)(431)"))
    result2 = perm_to_str(to_cycle(5, "(134)(143)(431)"))
    print([result1, result2])

    result1 = perm_to_str(to_cycle(5, "(143)(134)(341)"))
    result2 = perm_to_str(to_cycle(5, "(143)(143)(341)"))
    print([result1, result2])

    result1 = perm_to_str(to_cycle(5, "(135)(134)(531)"))
    result2 = perm_to_str(to_cycle(5, "(135)(143)(531)"))
    print([result1, result2])

    result1 = perm_to_str(to_cycle(5, "(153)(134)(351)"))
    result2 = perm_to_str(to_cycle(5, "(153)(143)(351)"))
    print([result1, result2])

    result1 = perm_to_str(to_cycle(5, "(145)(134)(541)"))
    result2 = perm_to_str(to_cycle(5, "(145)(143)(541)"))
    print([result1, result2])