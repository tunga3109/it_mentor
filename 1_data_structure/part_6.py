
# алгоритм бинарного поиска
def binary_search(arr, target):
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        mid_value = arr[mid]

        if mid_value == target:
            return mid  
        elif mid_value < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1 

sorted_array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target_value = 7

result = binary_search(sorted_array, target_value)

if result != -1:
    print(f"Значение {target_value} найдено по индексу {result}.")
else:
    print(f"Значение {target_value} не найдено.")


# алгоритм пузырьковой сортировки
def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

unsorted_array = [64, 34, 25, 12, 22, 11, 90]
print("Исходный массив:", unsorted_array)

bubble_sort(unsorted_array)

print("Отсортированный массив:", unsorted_array)
