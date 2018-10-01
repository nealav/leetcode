def binary_search(A, t): #args: A -> sorted array, t -> target
    left, right = 0, len(A) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if A[mid] < t:
            left = mid + 1
        elif A[mid] > t:
            right = mid - 1
        else:
            return mid
    return -1

if __name__ == '__main__':
    print(binary_search([1, 2, 3, 4, 5], 3))