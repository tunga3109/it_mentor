

arr = [64, 25, 12, 22, 11]
n = len(arr)

for i in range(n):
    # Последние i элементов уже отсортированы, поэтому их не рассматриваем
    for j in range(0, n-i-1):
        # Сравниваем пару элементов и меняем их местами, если нужно
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]