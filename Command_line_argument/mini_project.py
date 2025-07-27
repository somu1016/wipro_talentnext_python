# Project 1

import sys
def calculate_happiness(like_str, dislike_str, numbers_str):
    like_numbers = set(map(int, like_str.split('-')))
    dislike_numbers = set(map(int, dislike_str.split('-')))
    numbers = map(int, numbers_str.split('-'))

    happiness = 0
    for number in numbers:
        if number in like_numbers:
            happiness += 1
        elif number in dislike_numbers:
            happiness -= 1

    return happiness

like_str = sys.argv[1]
dislike_str = sys.argv[2]
numbers_str = sys.argv[3]
final_happiness = calculate_happiness(like_str, dislike_str, numbers_str)
print(final_happiness)