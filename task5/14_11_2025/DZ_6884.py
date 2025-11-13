ans = []
for n in range(1,100_000):
    z = bin(n)[2:]
    if n % 2 == 0:
        z = '1' + z + '0'
    else:
        z = '11' + z + '11'
    r = int(z,2)
    if r > 225:
        ans.append(r)
print(min(ans))

#228