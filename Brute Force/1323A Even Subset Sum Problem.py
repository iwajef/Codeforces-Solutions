
def existsEvenSubset(arr):
    n = len(arr)
    ans_indices = []
    i = 0
    j = 0
    while i < n and j < n:
        subset_sum = sum(arr[i:j + 1])
        if subset_sum % 2 != 0:
            j += 1
        else:
            for index in range(i, j + 1):
                ans_indices.append(index + 1)
            break
        if j == n:
            i += 1
            j = i

    if len(ans_indices) != 0:
        return ans_indices
    else:
        return -1


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr_str = input().split(' ')
        arr = []
        for elem in arr_str:
            arr.append(int(elem))
        ans = existsEvenSubset(arr)
        if ans != -1:
            print(len(ans))
            for num in ans:
                print(num, end=' ')
            print()
        else:
            print(-1)
