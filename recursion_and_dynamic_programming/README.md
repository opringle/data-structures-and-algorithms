# Recursion & Dynamic Programming

## Bottom-Up Approach

*How can you build the case from the previous case?*

Think about how you can build a solution from the bottom up. For example, when a list only contains 1 or 0 elements. Then think about how to solve for 2 elements. Eventually you'll realize what the recursive call should be.

## Top-Down Approach

Think about how you can divide the problem for case N into subproblems.

## Half and half approach

Often effective to divide the dataset in half. Recurse on each half of the input. Eg binary search. Merge sort works like this too.

## Recursive vs iterative problems

Recursive functions can be space intensive because each recursive call adds a new layer to the stack. If your function uses constant space but has N recursive calls, it uses O(N) space.

Often you can save space by avoiding recursive approaches.

## Dynamic Programming & Memoization

Dynamic programming is mostly just taking a recursive algorithm and finding overlapping subproblems. You then cache those results for future calls.

```python
def recursive_fibonacci(n: int):
    if i == 0:
        return 0
    elif i == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
```

The runtime of this function is O(2^n). This is clear if you draw the recursive tree for the function. There are n levels each with a max of 2 children.

Drawing the recursive tree, we see many of the calls are computed more than once.

### Top-Down Dynamic Programming (Memoization)

Here we simly cache the results as we go.

```python
def fibonacci(n: int):
    return dynamic_fibonacci(n, [0]*n)

def dynamic_fibonacci(n: int, memo: List[int]):
    if n < 2:
        return n
    
    result = memo[i]
    if result == 0:
        # compute and store the result
        memo[i] = fibonacci(n-1, memo) + fibonacci(n-2, memo)
    else:
        return result
```

### Bottom-Up Dynamic Programming

```python
def fibonacci(n: int) -> int:
    if n < 2:
        return n
    
    memo = [0] * (n+1)
    memo[1] = 1
    for i in range(2, n + 1):
        memo[i] = memo[i-1] + memo[i-2]
    return memo[n-1] + memo[n-2]
```

