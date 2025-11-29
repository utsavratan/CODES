x = 10
print(f"Initial value of x: {x}")
operations = [
    ('+=', 5),
    ('-=', 3),
    ('*=', 2),
    ('/=', 4),
    ('//=', 2),
    ('%=', 3)
]
for op, value in operations:
    exec(f"x {op} {value}")
    print(f"After x {op} {value}: {x}")
x = 10
print(f"\nReset x to: {x}")
x //= 3
print(f"After x //= 3: {x}")
a="krmangalamuniversity"
b=len(a)
b=upper.case(a)
print(b)