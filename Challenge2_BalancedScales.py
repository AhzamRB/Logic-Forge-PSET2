
def can_balance_scales(arr):
    arr.sort()
    for i in range(len(arr)):
        left_sum = sum(arr[:i])
        right_sum = sum(arr[i:])
        if left_sum == right_sum:
            return True
    return False




arr = [1, 5, 11, 5]
print(can_balance_scales(arr))
arr = [1, 3, 5]
print(can_balance_scales(arr)) 