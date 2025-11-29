def print_diamond(height):
    for i in range(height):
        print(' ' * (height - i - 1), end='')
        print('*' * (2 * i + 1))
    for i in range(height - 2, -1, -1):
        print(' ' * (height - i - 1), end='')
        print('*' * (2 * i + 1))
print_diamond(3)
