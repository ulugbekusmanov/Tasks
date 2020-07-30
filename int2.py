
n = 4
s = ''

if n % 2 == 0:
    s = "a" * (n - 1)
    s += "b"
else:
    s = 'a' * n
print(s)
