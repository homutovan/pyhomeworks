import time

# factorial
# 0 -> 0
# 1 -> 1
# 2 -> 2
# 3 -> 6
# 6 -> 6 * func(5)

def factorial_cycle(n: int) -> int:
    """"""
    res = 1

    for i in range(n + 1):
        if i == 0:
            i = 1
        res = res * i

    return res

def factorial_rec(n: int) -> int:
    """"""
    if n == 0:
        return 1
    return n * factorial_rec(n - 1)


for n in range(11):
    # res = factorial_rec(n)
    res = factorial_cycle(n)
    print(res)

# def idiotic_func(count=0):
#     print(f"I`m Idiot: {count}")
#     # time.sleep(0.4)
#     count += 1
#     idiotic_func(count)

# idiotic_func()