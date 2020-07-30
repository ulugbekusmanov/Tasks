def digital_root(n):
    total = 0
    for i in n:
        total += int(i)
    if total > 10:
        return digital_root(str(total))

    return total


