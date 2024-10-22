import random

# Fast raise power algorithm
def fast_raise_power(a, m, n):
    # first convert the powers value to binary
    mb = bin(m)[2:] # mb is the binary string of m
    result = 1
    for i in range(len(mb)-1, -1, -1):
        if mb[i] == '1':
            result *= a
            result %= n
        a = (a * a) % n # if binary is 0, do nothing but square and mod
    return result

# Quick Prime Check
def primality_check(n):
    for i in range(100):
        # randomly pick a number between 1 and n
        a = random.randrange(1, n)
        if fast_raise_power(a, n-1, n) != 1:
            return False
    return True

# get a prime of n digits 
def random_prime(n):
    lower = 10**n
    higher = 10**(n+1)
    while True:
        p = random.randrange(lower, higher)
        if primality_check(p):
            return p

def random_integer(p):
    return random.randrange(2, p-2)

# choose a large prime p with 16 digits
p = random_prime(20)

# choose an integer alpha 
alpha = random_integer(p)

# get private key a, b 
a = random_integer(p)
b = random_integer(p)

# compute public keys
A = fast_raise_power(alpha, a, p)
B = fast_raise_power(alpha, b, p)

# get K_AB
Ka = fast_raise_power(B, a, p)
Kb = fast_raise_power(A, b, p)

print(len(str(Ka)))

def hex_to_bin(hex):
    binary = bin(int(hex, 16))[2:]
    return binary


print(len(str("26198494662568aaa")))