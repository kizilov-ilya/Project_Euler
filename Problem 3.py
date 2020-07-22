# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

number = 600851475143
results = []
for i in range(number):
    if number % (i + 1) == 0:
        results.append(i + 1)
        print(i + 1)
print(max(results))

# Instagram, ProjectEuler.net: ilya._romanovich
# Telegram: @kizilov_elijah
