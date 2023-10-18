def gcd(m,n):
    if m < n:
        temp = n
        n = m
        m = temp
    r = m % n
    if r == 0:
        return f"{n} is the GCD of m"
    else:
        return gcd(n,r)


print(gcd(12,256))
