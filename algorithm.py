

def common_search(text, pattern):
    t_l = len(text)
    p_l = len(pattern)
    if p_l == 0 or p_l > t_l:
        return None

    for i in range(t_l - p_l):
        for j in range(p_l):
            if text[i] != pattern[j]:
                break
        if j == p_l - 1:
            return i
    return None


def partial_value(pattern):
    p_l = len(pattern)
    p_v = [0]
    k = 0
    for i in range(1, p_l):
        while k > 0 and pattern[i] != pattern[k]:
            k = p_v[k]

        if pattern[i] == pattern[k]:
            p_v.append(k + 1)
            k += 1
        else:
            p_v.append(0)

    return p_v


def kmp(text, pattern):
    t_l = len(text)
    p_l = len(pattern)
    if p_l == 0 or p_l > t_l:
        return -1

    p_v = partial_value(pattern)

    j = 0
    for i in range(t_l):
        while j > 0 and pattern[j] != text[i]:
            j =  p_v[j-1]

        if pattern[j] == text[i]:
            j += 1

        if j == p_l:
            return i - p_l + 1

    return -1

