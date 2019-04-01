def count_hi(str):
    c = 0
    for i in range(len(str) - 1):
        if str[i:i + 2] == "hi":
            c += 1
    return c