print("Adjon meg egy szamot!")
x = int(input())

# dynamically typed (reassigned x)
# lists can contain any type (even mixed)
x = [3,6,1,"alma",5] + ["sad"] # concating lists
print(x[3])
print(x[1:3]) # prints indices 1 and 2
print(x[:2]) # prints till indice 2 (exclusive)
print(x[1:]) # prints from 1st index (inclusive)

x += [4]

# for loops
out = ""
for i in range(10):
    out += str(i) + " "
out += "\n"
for i in range(3, 10, 2): # where to start, till when to go, step
    out += str(i) + " "

print(out)

# continue, break, prime
# determines whether a number is prime
def isPrime(number):
    i = 2
    while i * i <= number:
        if number % i == 0:
            return False
        
        i += 1
    
    return True

for i in range(20):
    if (i % 3 == 0):
        continue # steps to next for step
    
    if (i == 17):
        break # exits for
    
    if isPrime(i):
        print(i, "is a prime number")
    else:
        print(i, "is a boring number")

# list generators
x = ["3", "5", "34", "5.5", "-1"]
y = [float(i) for i in x] # converts strings to floats

print("From", x, "to", y)

# perfect numbers
print([i for i in range(6, 10_000) if i == sum([k for k in range(1, i) if i % k == 0])])