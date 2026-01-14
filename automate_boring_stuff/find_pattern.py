import re

phone_num_pattern_obj = re.compile(r'(\d{3})-(\d{10})') # addin parenthesis will divide the string into groups.
match_obj = phone_num_pattern_obj.search("My number is +977-1233456789.")
# match_obj = phone_num_pattern_obj.findall('')  Return all possible matches

print(match_obj.group(2))

vowel_pattern = re.compile(r'[aeiouAEIOU]')

print(vowel_pattern.findall("HELLO, world")) # Returns all the vowel in a string.

pattern = re.compile(r'42!?') # Here ! is optional since it's followed by ?.
pattern = re.compile(r'(Ha){3}') # HaHaHa
pattern = re.compile(r'(Ha){3, 5}') # (HaHaHa, Ha*4, Ha*5) will always return longest match. 
pattern = re.compile(r'(.*)') # Match everything but greedy.
pattern = re.compile(r'(.*)?') # Match everything but no greedy.

'''
\d : For numeric value 0-9                  \D : Not 0-9  
\w : Letters, numbers and underscore        \W : Not <-
\s : Space, tab or newline character        \S : Not <-
^ : Begins with                              $ : Ends with
\b : match word in a boundary
'''
pattern = re.compile(r'\bcat.*?\b') # Match words beginning with cat
pattern = re.compile(r'pararara', re.I) # Case-insensitive

