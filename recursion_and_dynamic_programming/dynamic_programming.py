from typing import List

def top_down_dynamic_fibonacci(n: int):
    return _top_down_dynamic_fibonacci(n, [0]*(n+1))

def _top_down_dynamic_fibonacci(n: int, memo: List[int]):
    if n < 2:
        return n

    if memo[n] == 0:
        memo[n] = _top_down_dynamic_fibonacci(n-1, memo) + _top_down_dynamic_fibonacci(n-2, memo)
    return memo[n]

def bottom_up_fibonacci(n: int) -> int:
    if n < 2:
        return n
    
    memo = [0] * (n+1)
    memo[1] = 1
    for i in range(2, n):
        memo[i] = memo[i-1] + memo[i-2]
    return memo[n-1] + memo[n-2]

if __name__ == '__main__':
    print(top_down_dynamic_fibonacci(6))
    print(bottom_up_fibonacci(6))