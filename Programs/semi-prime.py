#!/usr/bin/env python

def is_semiprime(n):
    for d1 in range(2, int(n**.5)+1):
        if n % d1 == 0:
            d2 = n / d1
            return is_prime(d1) and is_prime(d2)
    return False

def is_prime(n):
  if n == 2 or n == 3: return True
  if n < 2 or n%2 == 0: return False
  if n < 9: return True
  if n%3 == 0: return False
  r = int(n**0.5)
  f = 5
  while f <= r:
    if n%f == 0: return False
    if n%(f+2) == 0: return False
    f +=6
  return True    

def ask_semiprime():
    num = int(input("What number would you like to check?"))
    if is_semiprime(num):
        print(num, " is semiprime")
    else:
        print(num, " is not semiprime")

ask_semiprime()