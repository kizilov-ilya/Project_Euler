# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

def solution(number):
    div = 2
    while div ** 2 <= number:  # this way I applied the factorization method without calculating the square root
        if number % div == 0:
            number //= div
            print(div)
        else:
            div += 1
    if number != 1:
        print(number)


n = 600851475143
solution(n)

# Instagram, ProjectEuler.net: ilya._romanovich
# Telegram: @kizilov_elijah
