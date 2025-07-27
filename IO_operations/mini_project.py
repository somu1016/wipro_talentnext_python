# Project 1:

from collections import Counter

def get_meeting_time(line_count):
    
    if line_count > 24 or line_count < 1:
        raise ValueError("Line count must be between 1 and 24.")
    if line_count > 12:
        return f"{line_count - 12} PM"
    return f"{line_count} AM"

def find_most_common_word(words):
    
    cleaned_words = [word.strip('.,!?;:"()').lower() for word in words if word.strip()]
    count = Counter(cleaned_words)
    most_common_word, frequency = count.most_common(1)[0]
    return most_common_word.capitalize(), frequency

def analyze_secret_message(filename):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            line_count = len(lines)

           
            words = []
            for line in lines:
                words.extend(line.split())

            
            meeting_time = get_meeting_time(line_count)

           
            common_word, frequency = find_most_common_word(words)
            meeting_place = f"{common_word} Street"

            
            print(f"\n Secret Meeting Details")
            print(f"Meeting time: {meeting_time}")
            print(f"Meeting place: {meeting_place}")
            print(f"\n Explanation:")
            print(f"Number of lines = {line_count}, so meeting time = {meeting_time}")
            print(f"Word '{common_word.lower()}' appeared {frequency} times, so place = {meeting_place}")

    except FileNotFoundError:
        print(f" Error: File '{filename}' not found.")
    except ValueError as ve:
        print(f" Error: {ve}")
    except Exception as e:
        print(f" An unexpected error occurred: {str(e)}")


if __name__ == "__main__":
    filename = input("Enter the filename: ")
    analyze_secret_message(filename)
