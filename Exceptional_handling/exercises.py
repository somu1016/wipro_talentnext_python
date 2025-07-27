#  1. Division with exception handling

def divide_numbers():
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        result = num1 / num2
        print("Result:", result)
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
    except ValueError:
        print("Error: Please enter valid numbers.")
    except Exception as e:
        print("Unexpected Error:", e)

divide_numbers()

# 2. Check if number is prime with input validation

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def check_prime():
    try:
        num = int(input("Enter a number: "))
        if is_prime(num):
            print(f"{num} is a prime number.")
        else:
            print(f"{num} is not a prime number.")
    except ValueError:
        print("Error: Please enter a valid integer.")

check_prime()

#  3. Open file and print content in title case

def read_and_title_case_file():
    try:
        filename = input("Enter file name: ")
        with open(filename, 'r') as file:
            content = file.read()
            print("Title Cased Content:\n")
            print(content.title())
    except FileNotFoundError:
        print("Error: File does not exist.")
    except Exception as e:
        print("Unexpected Error:", e)

read_and_title_case_file()

# 4. Check index in list and validate number sign

def index_check():
    nums = [3, -5, 8, 0, -2, 9, 6, -4, 1, 7]
    try:
        index = int(input("Enter an index (0-9): "))
        number = nums[index]
        if number >= 0:
            print(f"The number at index {index} is positive: {number}")
        else:
            print(f"The number at index {index} is negative: {number}")
    except IndexError:
        print("Error: Index out of range.")
    except ValueError:
        print("Error: Please enter a valid integer.")
    except Exception as e:
        print("Unexpected Error:", e)

index_check()



