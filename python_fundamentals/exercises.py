# 1 Python program that checks whether a given number is positive, negative, or zero:


num = float(input("Enter a number: "))

if num > 0:
    print("The number is positive")
elif num < 0:
    print("The number is negative")
else:
    print("The number is zero")
    
# 2 Python program that checks whether a given number is even or odd:

num = int(input("Enter a number: "))

if num % 2 == 0:
    print(f"{num} is an even number")
else:
    print(f"{num} is an odd number")
    
# 3 Python Program to Check if Two Numbers Have the Same Last Digit:

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

last1 = num1 % 10
last2 = num2 % 10

if last1 == last2:
    print(f"True - Both numbers end with {last1}")
else:
    print(f"False - {num1} ends with {last1} and {num2} ends with {last2}") 
    
# 4 Python program that prints numbers from 1 to 10 in a single row with one tab space

for i in range(1, 11):
    print(i, end='\t')

# 5  Python program that prints all even numbers between 23 and 57, each on a separate line:

for num in range(23, 58):
    if num % 2 == 0:
        print(num)

# 6 Python program to check if a given number is prime or not:

num = int(input("Enter a number: "))

is_prime = True  

if num <= 1:
    is_prime = False  
else:
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break  

if is_prime:
    print(num, "is a prime number")
else:
    print(num, "is not a prime number")
    
# 7 Python program to print all prime numbers between 10 and 99:

for num in range(10, 100):
    is_prime = True

    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        print(num)
        
#  8  Python program to find the sum of all digits of a given number:
number = int(input("Enter a number: "))
sum_of_digits = 0
temp = abs(number) 

while temp > 0:
    digit = temp % 10  
    sum_of_digits += digit
    temp = temp // 10 

print(f"Sum of digits of {number} is: {sum_of_digits}")


# 9 Python Program to reverse a number and print :

number = int(input("Enter a number: "))
reversed_num = 0
temp = abs(number) 

while temp > 0:
    digit = temp % 10  
    reversed_num = reversed_num * 10 + digit
    temp = temp // 10  


if number < 0:
    reversed_num = -reversed_num

print(f"Reversed number: {reversed_num}")

# 10 Python program to check if a number is a palindrome or not:

num = int(input("Enter a number: "))
original = abs(num)
reverse = 0
temp = original

while temp > 0:
    digit = temp % 10
    reverse = reverse * 10 + digit
    temp = temp // 10

if original == reverse:
    print(f"{num} is a palindrome")
else:
    print(f"{num} is not a palindrome")



