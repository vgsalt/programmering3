rangeinput = int(input("Hvor lenge vil du at Fibonacci-sekvensen skal gå? "))

shit = []

def fibonacci(n):
    if n in {0, 1}:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

for i in range(rangeinput):
    shit.append(fibonacci(i))

print(shit)