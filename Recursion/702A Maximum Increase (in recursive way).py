
def solve(n, arr):
    for i in range(n - 1):
        if arr[i] >= arr[i + 1]:
            ans1 = solve(i + 1, arr[:i + 1])
            ans2 = solve(n - i - 1, arr[i + 1:])
            ans = max(ans1, ans2)
            return ans
    return n
