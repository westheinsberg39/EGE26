ans = []
for n in range(1,100_000):
    r = f'{n:b}'
    z = sum(map(int,r))
    if z % 2 == 0:
        r = r + '0'
        r = '10' + r[2:]
    else:
        r = r + '1'
        r = '11' + r[2:]
    r = int(r,2)
    if r < 35:
        print(n)
        ans.append(n)

print(max(ans))
# + метод с ans