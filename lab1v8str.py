a = (
    int(input()),int(input()),int(input()),int(input()),int(input()),int(input())
)
b = (1, 1, 1, 0.75, 0.5, 0)
print(
    2
    * (
        a[0] * b[0]
        + a[1] * b[1]
        + a[2] * b[2]
        + a[3] * b[3]
        + a[4] * b[4]
        + a[5] * b[5]
    )
)
