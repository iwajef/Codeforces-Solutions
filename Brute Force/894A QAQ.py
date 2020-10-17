
def solve(s):
    if len(s) < 3:
        return 0
    ans = 0
    for i in range(len(s)):
        for j in range(i + 1, len(s)):
            for k in range(j + 1, len(s)):
                if s[i] == 'Q' and s[j] == 'A' and s[k] == 'Q':
                    ans += 1
    return ans

if __name__ == '__main__':
    s = input()
    ans = solve(s)
    print(ans)
    