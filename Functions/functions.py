# 1. Sum of all numbers in a list

def sum_of_list(numbers):
    return sum(numbers)

def main():
    input_str = input("Enter numbers separated by spaces: ")
    sample_list = list(map(int, input_str.split()))
    result = sum_of_list(sample_list)
    print("Sum:", result)

main()

#  2. Reverse of a string

def reverse_string(s):
    return s[::-1]

def main():
    sample = input("Enter a string to reverse: ")
    result = reverse_string(sample)
    print("Reversed String:", result)

main()


# 3. Factorial of a number

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def main():
    number = int(input("Enter a non-negative integer: "))
    if number < 0:
        print("Factorial is not defined for negative numbers.")
    else:
        print("Factorial of", number, "is", factorial(number))

main()

# 4. Count uppercase and lowercase letters

def count_case(s):
    upper = lower = 0
    for char in s:
        if char.isupper():
            upper += 1
        elif char.islower():
            lower += 1
    print("Uppercase letters:", upper)
    print("Lowercase letters:", lower)

def main():
    sample = input("Enter a string: ")
    count_case(sample)

main()

#  5. Print even numbers from a list

def print_even_numbers(numbers):
    even_numbers = [num for num in numbers if num % 2 == 0]
    print("Even Numbers:", even_numbers)

def main():
    input_str = input("Enter list elements separated by spaces: ")
    sample_list = list(map(int, input_str.split()))
    print_even_numbers(sample_list)

main()

# 6. Check if a number is prime

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def main():
    number = int(input("Enter a number to check if it's prime: "))
    if is_prime(number):
        print(number, "is a prime number")
    else:
        print(number, "is not a prime number")

main()


