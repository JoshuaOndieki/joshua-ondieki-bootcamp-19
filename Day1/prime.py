#prime numbers generator

from math import sqrt

def prime_numbers(upper_limit):
    prime_list=[]
    def is_prime(n):  # prime checker
        sqrt_=sqrt(n)
        if n < 2:
            return False
        elif n==2:
            return True
        for i in range(2,n):
            if n%i==0:
                return False
            if sqrt_<i: #minimize the numbers to be checked for efficiency
                break
        return True
    try:
        if upper_limit<0:
            return "No prime numbers within that range! All prime numbers are positive"
        for number in range(upper_limit+1):
            if is_prime(number):
                prime_list.append(number)
        return prime_list
    except TypeError:
        raise TypeError
