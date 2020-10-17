
def maxNonDecreasingSubsegment(arr):
    
    n = len(arr)
    ans = 0
    tmp = 1
    for i in range(1, n):
        if arr[i] >= arr[i - 1]:
            tmp += 1
        else:
            ans = max(ans, tmp)
            tmp = 1
    
    return max(ans, tmp)


if __name__ == '__main__':

    n = int(input())
    arr_str_list = input().split(' ')
    arr = []
    for elem in arr_str_list:
        arr.append(int(elem))
    ans = maxNonDecreasingSubsegment(arr)
    print(ans)
