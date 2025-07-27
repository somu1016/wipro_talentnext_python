# 1. Read entire content from a file and display it

filename = input("Enter filename: ")
try:
    with open(filename, 'r') as file:
        content = file.read()
    print("File content:")
    print(content)
except FileNotFoundError:
    print(f"ERROR: The file '{filename}' was not found. Please check the filename and try again.")
except PermissionError:
    print(f"ERROR: You don't have permission to read '{filename}'.")
except Exception as e:
    print(f"An unexpected error occurred: {str(e)}")
    
    
# 2. Read first 'n' lines from a file (user specifies n)

filename = input("Enter filename: ")
n = int(input("How many lines to read? "))
with open(filename, 'r') as file:
    for i in range(n):
        line = file.readline()
        if not line:
            break
        print(line, end='')
        
# 3. Accept user input and append to a file

filename = input("Enter filename: ")
text = input("Enter text to append: ")
with open(filename, 'a') as file:
    file.write(text + '\n')
print("Text appended successfully")

# 4. Read file line by line into a list

filename = input("Enter filename: ")
lines = []
with open(filename, 'r') as file:
    for line in file:
        lines.append(line.strip())
print("File contents as list:")
print(lines)

# 5. Find the longest word in a file (assuming one longest word)

filename = input("Enter filename: ")
with open(filename, 'r') as file:
    words = file.read().split()
longest = max(words, key=len)
print(f"Longest word: {longest}")

# 6. Count frequency of a word in a file

filename = input("Enter filename: ")
search_word = input("Enter word to search: ").lower()
count = 0
with open(filename, 'r') as file:
    for line in file:
        words = line.lower().split()
        count += words.count(search_word)
print(f"'{search_word}' appears {count} times")