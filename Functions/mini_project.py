# Project 1:

def sort_colors(color_sequence):
    
    colors = color_sequence.split('-')
    colors.sort()
    return '-'.join(colors)


user_input = input("Enter colors separated by hyphens : ")


sorted_colors = sort_colors(user_input)
print("Sorted colors:", sorted_colors)


# Project 2:

def ispalindrome(name):
    return name == name[::-1]

def count_the_vowels(name):
    
    vowels = 'aeiou'
    return sum(1 for char in name.lower() if char in vowels)

def frequency_of_letters(name):
    
    freq = {}
    for char in name.lower():
        if char.isalpha():  
            freq[char] = freq.get(char, 0) + 1
    return freq

def analyze_name(name):
    
    palindrome_result = "Yes it is a palindrome." if ispalindrome(name) else "No it is not a palindrome."
    
   
    vowel_count = count_the_vowels(name)
    
    
    freq = frequency_of_letters(name)
    freq_str = ', '.join(f"{k}-{v}" for k, v in sorted(freq.items()))
    
    
    print(palindrome_result)
    print(f"No of vowels: {vowel_count}")
    print(f"Frequency of letters: {freq_str}")

def main():
    print("Welcome to the Name Analysis Program!")
    name = input("Enter a name: ").strip()
    
    
    
    analyze_name(name)

if __name__ == "__main__":
    main()