def print_max(a, b):
    if a > b:
        print(a, "is maximum")
    elif a == b:
        print(a, "is equal to", b)
    else:
        print(b, "is maximun")

print_max(3, 4)
print_max(3, 3)
print_max(5, 2)