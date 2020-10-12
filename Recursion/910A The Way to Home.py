
def solve(n, d, s):

    if len(s) <= d or len(s) - 1 == d:
        return 1
    
    indices = []
    for i in range(1, d + 1):
        if s[i] == '1':
            indices.append(i)
    
    if len(indices) == 0:
        print(-1)
        exit(0)
    
    index = max(indices)
    ans = solve(n - index, d, s[index:]) + 1
    return ans


if __name__ == '__main__':
    tmp = input().split(' ')
    n = int(tmp[0])
    d = int(tmp[1])
    s = input()
    ans = solve(n, d, s)
    print(ans)
