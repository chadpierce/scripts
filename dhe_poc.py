#diffie hellman poc

g =96   # pub prime base
p = 7348  # pub prime modulus
a = 43   # alice priv
b = 15967  # bob priv

A = g**a % p # alive pub
B = g**b % p # bob pub

print('g ', g)
print('p ', p)
print('a ', a)
print('b ', b)

print('A ', A)
print('B ', B)

sa = B**a % p
sb = A**b % p

print('sa ', sa)
print('sb ', sb)
