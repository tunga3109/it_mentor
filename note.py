

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 2
low, high = 0, len(arr) - 1

while low <= high:
    mid = (low + high) // 2
    mid_value = arr[mid]

    if mid_value == target:
        print(mid)  
    elif mid_value < target:
        low = mid + 1
    else:
        high = mid - 1
        
a = -1

if a != -1:
    print(f"Значение {target} найдено по индексу {mid}.")
else:
    print(f"Значение {target} не найдено.")