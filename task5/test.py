def convert(sys,num):
    r = ''
    if sys == 0:
        return '0'
    while sys > 0:
        r +=  str(sys % num)
        sys //= num
    return r[::-1]

convert(2,8)
print(convert(8,2))