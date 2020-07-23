# A palindromic number reads the same both ways.
# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

def is_palindrome(s):
    return s == s[::-1]


def solution():
    answers = []
    for n in range(999, 99, -1):
        for m in range(999, 99, -1):
            p = n * m  # decide to add one more variable to avoid re-calculations
            if is_palindrome(str(p)):
                print(f"Palindrome! {n} x {m} = {p}")
                answers.append(int(p))
    return answers


print(f'answer is {max(solution())}')
# Instagram, ProjectEuler.net: ilya._romanovich
# Telegram: @kizilov_elijah
