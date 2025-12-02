#1
a = 3 
b = 5
sum = a + b
print (sum)
#2
my_string_1 = 'Hello, World!'
reversed_string = my_string_1[::-1]
print(reversed_string)
#3
my_string_2 = 'Hello, World!'
length = len(my_string_2)
print(length)
#4
my_string_3 = 'Hello, '
my_string_4 = 'World!'
concatenated_string = my_string_3 + my_string_4
print(concatenated_string)
#5
character = 'e'
character_lower = character.lower()
if character_lower in ('a', 'e', 'i', 'o', 'u'):
    is_vowel = True
else:
    is_vowel = False    
if is_vowel == True:
    print(f"The character '{character}' is a vowel.")
else:
    print(f"The character '{character}' is not a vowel.")
#6
original_string = "hello"
if len(original_string) >= 2:
     modified_string = original_string[-1] + original_string[1:-1] + original_string[0]  
else:
    modified_string = original_string
print(modified_string)
#7
my_string_5 = "hello world"
uppercase_string = my_string_5.upper()
print(uppercase_string)
#8
rectangle_length = 4
rectangle_width = 6
area = rectangle_length * rectangle_width
print(area)
#9
my_number = 10
if my_number % 2 == 0:
    result = "even"
else:
    result = "odd"
print(f"The number {my_number} is {result}.")
#10
my_string_6 = "Hello World"
extracted_chars = my_string_6[0:3]
print(extracted_chars)
#11
name = "Alice"
age = 30
message = f"Hello, my name is {name} and I am {age} years old."
print(message)
#12
my_string_7 = "New_String"
extracted_chars = my_string_7[2:6]
print(extracted_chars)
#13
number_as_string = "123"
converted_integer = int(number_as_string)
print(converted_integer)
#14
my_string_8= "Hello"
repeated_string = my_string_8 * 3
print(repeated_string)
#15
number_1 = 15
number_2 = 2
quotient = number_1 // number_2
remainder = number_1 % number_2
print(f"The first number is: {number_1}")
print(f"The second number is: {number_2}")
print(f"The quotient is: {quotient}")
print(f"The remainder is: {remainder}")
#16
number_3 = 25
number_4 = 6
float_division = number_3 / number_4
print(float_division)
#17
my_string = "Hello, world!"
char_to_find = 'o'
occurrence_count = my_string.count(char_to_find)
print(f"The character '{char_to_find}' appears {occurrence_count} times in the string.")
#18
my_string = "He said, \"Hello, World!\""
print(my_string)
#19
my_string = """-Hello, World!
-Yes hellow
-World"""
print(my_string)
#20
base = 5
exponent = 3
power_result = base ** exponent
print(power_result)
#21
palindrome_string = "racecar"
is_palindrome = palindrome_string == palindrome_string[::-1]
print(is_palindrome)
#22
def are_anagrams_ignore_case(s1, s2):
    s1_lower = s1.lower()
    s2_lower = s2.lower()
    if len(s1_lower) != len(s2_lower):
        return False
    else:
        return sorted(s1_lower) == sorted(s2_lower)
print(are_anagrams_ignore_case("Listen", "Silent"))
print(are_anagrams_ignore_case("Listenn", "Silentt"))