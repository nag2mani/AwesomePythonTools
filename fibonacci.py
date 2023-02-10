#Method=01
n=int(input("entre your number:"))
def fibonacci_numbers(x):
	if x == 0:
		return 0
	elif x == 1:
		return 1
	else:
		return fibonacci_numbers(x-2)+fibonacci_numbers(x-1)

for i in range(0, n):
	print(fibonacci_numbers(i), end=" ")



#Method=02
def fibonacci_numbers(n):
	fib = [0, 1]
	for k in range(2,n):
		fib.append(fib[-1] + fib[-2])
	return fib
print(fibonacci_numbers(5))



#Method=03
def fibonacci_numbers(n):
    fib = [0, 1]
    while len(fib) < n:
        fib.append(fib[-1] + fib[-2])
    return fib
print(fibonacci_numbers(5))



#Method=04
n=int(input("entre your number:"))
x=0
y=1
z=0
for i in range (n):
	x=y
	y=z
	z=x+y
	print(z,end=',')





