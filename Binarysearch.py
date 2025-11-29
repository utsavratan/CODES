def binary_search(arr, x, low, high):
    if high >= low:
        mid = low + (high - low) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binary_search(arr, x, low, mid - 1)
        else:
            return binary_search(arr, x, mid + 1, high)
    return -1

def main():
    print("Enter a sorted list of numbers (space-separated):")
    try:
        arr = list(map(int, input().strip().split()))
    except ValueError:
        print("Invalid input.")
        return

    try:
        x = int(input("Enter number to search: "))
    except ValueError:
        print("Invalid input.")
        return

    index = binary_search(arr, x, 0, len(arr) - 1)
    if index != -1:
        print(f"\nFound at Index No.{index}")
    else:
        print("\nNumber not found.")

if __name__ == "__main__":
    main()