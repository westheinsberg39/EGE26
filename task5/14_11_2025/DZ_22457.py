ans = []
def convert(n, b):
    r = ''
    if n == 0:
        return '0'
    while n > 0:
        r += str(n % b)
        n //= b
    return r[::-1]


for n in range(1,100000):
    r_7 = convert(n, 7)

    s = sum(map(lambda x: int(x, 7), r_7))

    if s % 2 == 0:
        r_7 = r_7 + '555'
    else:
        r_7 = '23' + r_7 + '6'

    r = int(r_7, 7)
    if r < 12717:
        ans.append(n)
print(max(ans))
#47