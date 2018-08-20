# https://www.learnpython.org/en/Loops
# For Loops

primes = [2, 3, 5, 7]
for prime in primes:
    print(prime)

print ("\n-----1. -----")

# Prints out the numbers 0,1,2,3,4
for x in range(5):
    print(x  , end="")

print("\n-----2. ----- ")

# Prints out 3,4,5
for x in range(3, 6):
    print(x , end="")

print("\n-----3. ----- ")

# Prints out 3,5,7 (start, stop, step(optional))
for x in range(3, 8, 2):
    print(x , end="")

print("\n--- While Loop Below")

#-------------------- While Loops -------------------------------


count = 0
while count < 5:
    print(count , end="")
    count += 1


print("\n----- Break Example ")
count = 0
while True:
    print(count, end="")
    count += 1
    if count >= 5:
        break

print("\n----- Continue Example Modulo ")
for x in range(10):
    # Check if x is even
    if x % 2 == 0:
        continue
    print(x, end="")


print("\n----- Loop with else ")
count=0
while(count<5):
    print(count,  end="")
    count +=1
else:
	print("\n")
	print("count value reached %d" %(count))


print("\n----- Loop with Break")
for i in range(1, 10):
    if(i%5==0):
        break
    print(i , end="")
else:
    print("this is not printed because for loop is terminated because of break but not due to fail in condition")



print("\n----- Loop with Continue")
data = [ 1, 3, 2 , 4 , 5]
for x in data:
	if x % 2 == 0:
		continue
	print(x, end="")