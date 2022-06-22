def binary_search(list, target):
    cnt = 0
    low = 0
    high = len(list) - 1
    while low <= high:
        mid = (low + high) // 2
        guess = list[mid]
        if guess == target:
            print(f'Number of checks: {cnt}')
            return mid
        if guess > target:
            high = mid - 1
        else:
            low = mid + 1
        cnt += 1
    return None

# n = int(input())
# l = [1, 3, 5, 7, 11, 13, 17, 21, 23, 25, 27, 31]
# print(binary_search(l, n))