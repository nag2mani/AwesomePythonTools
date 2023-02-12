'''
Write a function is_prime(n) that receives a number n as parameter and returns True if n is prime, else returns False.
'''

# # By me:
def is_prime(n):
    if n==2 or n==3:
        return True
    for x in range(2,n):
        if n%x==0:
            return False
    return True

print(is_prime(23))
print(is_prime(97))
print(is_prime(99999989))
# print(is_prime(9999999967))



# ## By ma'am:-
import math
def is_prime(n):
    if n==2 or n==3:
        return True
    for x in range(2,math.ceil(math.sqrt(n))+1):
        if n%x==0:
            return False
    return True

print(is_prime(23))
# print(is_prime(97))
# print(is_prime(99999989))
# print(is_prime(9999999967))




