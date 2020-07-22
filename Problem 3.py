
number = 600851475143
results = []
for i in range(number):
    if number % (i+1) == 0:
        results.append(i+1)
        print(i+1)
print(max(results))
