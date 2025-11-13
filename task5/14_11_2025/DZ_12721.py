ans = []

def convert(sys, num):
    r = ''
    if sys == 0:
        return '0'
    while sys > 0:
        r = str(sys % num) + r
        sys //= num
    return r

for n in range(1, 100_000):
    r_8 = convert(n, 8)

    count = r_8.count('0') + r_8.count('2') + r_8.count('4') + r_8.count('6')

    if count % 2 != 0:
        r_8 = r_8 + '46'
    else:
        ostatok = n % 8
        res = ostatok * 5

        oct = convert(res, 8)

        r_8 = oct + r_8

    R = int(r_8, 8)

    if n >= 80:
        ans.append(R)

print(min(ans))