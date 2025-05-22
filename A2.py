n = input("Enter numbers separated by spaces: ")

numbers = list(map(int, n.split()))
total = sum(numbers)
print("Sum of all numbers:", total)
print()

text = input("Enter a string: ")

reversed_text = ""
for char in text:
    reversed_text = char + reversed_text  # prepend each character

print("Reversed string:", reversed_text)
print()

text = input("Enter a string: ")

vowels = "aeiouAEIOU"
vowel_count = 0

