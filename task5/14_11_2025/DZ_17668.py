ans = []
for n in range(1,100_000):
    z = f'{n:b}'
    if z.count('1') % 2 == 0:
        z = '10' + z[2:] + '0'
    else:
        z = '11' + z[2:] + '1'
    r = int(z,2)
    if n > 27:
        ans.append(r)
print(min(ans))
#42