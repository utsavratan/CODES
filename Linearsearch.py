def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i  
    return -1  

numbers = [10, 25 , 80 , 30, 45, 50 ,60]
search_for = 45

result = linear_search(numbers, search_for)

if result != -1:
    print(f"Element {search_for} found at index {result}")
else:
    print(f"Element {search_for} not found in the list")
    