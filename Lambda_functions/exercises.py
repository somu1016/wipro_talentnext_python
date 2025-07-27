# Lambda functions
# python code to cube each element in a list using a lambda function:

list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
cube = lambda x: x**3
cubed_list = [cube(num) for num in list_1]

print("Original list:", list_1)
print("Cubed list:", cubed_list)

# List comprehension
# 1. Odd Numbers Dictionary with Cubes

input_list = [1, 2, 3, 4, 5, 6, 7]

odd_cubes = {num: num**3 for num in input_list if num % 2 != 0}

print("Odd numbers with their cubes:")
print(odd_cubes)

# 2. Alphabet to Integer Mapping

alphabet_dict = {chr(97+i): i+1 for i in range(26)}

print("Alphabet to integer mapping:")
print(alphabet_dict)
