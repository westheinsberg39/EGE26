ans = [] # созд список для хран всех чисел
for n in range(1,100_000): # натур числа от 1
    r = f'{n:b}'
    if n % 3 == 0:
        r = r + r[-3:]
    else:
        r = r + bin(n % 3 * 3)[2:]
    r = int(r,2)
    if r <= 170:
        ans.append(r) #доб

print(max(ans)) # вывод max знач из списка