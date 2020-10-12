
if __name__ == '__main__':

    n = int(input())

    ans = 0
    denominations = [100, 20, 10, 5, 1]
    i = 0
    while n > 0:
        if n / denominations[i] >= 1:
            ans += n // denominations[i]
            n -= (n // denominations[i] * denominations[i])
        else:
            i += 1
    
    print(ans)

