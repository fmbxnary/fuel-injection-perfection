def priority(n):
    count = 0
    while (n % 2 == 0):
        count += 1
        n = n // 2
    return count


def solution(n):
    n = int(n)
    count = 0
    while (n != 1):
        if (n % 2 == 0):
            n //= 2
        elif (priority(n + 1) > priority(n - 1) and n > 3):
            n = n + 1
        else:
            n = n - 1
        count += 1
    return count
