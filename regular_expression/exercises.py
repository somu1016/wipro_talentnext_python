# 1. Check if string has only octal digits

strings = ['789', '123', '004']
for s in strings:
    if all(ch in '01234567' for ch in s):
        print(f"{s} is octal")
    else:
        print(f"{s} is not octal")

# 2. Extract user ID, domain name and suffix from email addresses

import re

emails = """zuck@facebook.com
sunder33@google.com
jeff42@amazon.com"""

pattern = r'(\w+)@(\w+)\.(\w+)'
matches = re.findall(pattern, emails)
print(matches) 

# 3 Split the following irregular sentence into proper words

import re

sentence = """A, very very; irregular_sentence"""
words = re.split(r'[;,_\s]+', sentence)
print(' '.join(words))  

# 4. Clean tweet (remove RT, mentions, URLs, hashtags, punctuations)

import re

tweet = '''Good advice! RT @TheNextWeb: What I would do differently if I was learning to code today http://t.co/lbwej0px0d cc: @garybernhardt #rstats'''

cleaned = re.sub(r'RT|cc', '', tweet)
cleaned = re.sub(r'@[A-Za-z0-9_]+', '', cleaned)
cleaned = re.sub(r'#\w+', '', cleaned)
cleaned = re.sub(r'http\S+', '', cleaned)
cleaned = re.sub(r'[^\w\s]', '', cleaned)

print(cleaned.strip())  

# 5. Extract all text between HTML tags

import requests # type: ignore
import re

r = requests.get("https://raw.githubusercontent.com/selva86/datasets/master/sample.html")
html_text = r.text

data = re.findall(r'>([^<]+)<', html_text)
cleaned_data = [item.strip() for item in data if item.strip()]
print(cleaned_data)

# 6. Words that begin and end with the same character

words = ['civic', 'trust', 'widows', 'maximum', 'museums', 'aa', 'as']
same_start_end = [word for word in words if word[0] == word[-1]]
print(same_start_end)  # Output: ['civic', 'aa']