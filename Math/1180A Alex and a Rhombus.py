
def solve(n):
    ans = 0
    tmp = 0
    for i in range(1, n):
        tmp += (2 * i - 1)
    ans = tmp * 2 + (2 * n - 1)
    return ans

if __name__ == '__main__':
    n = int(input())
    ans = solve(n)
    print(ans)
    