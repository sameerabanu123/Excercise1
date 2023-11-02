# Task #1
# Palindrome Checker:
# Create a function that checks if a given string is a palindrome (reads the same forwards and backward). 121
# Example - pramod
# madam - reverse(madam) -> same

string_name=input("enter the string for palindrome:")
def is_palindrome(string_name):
   reverse_string=string_name[::-1]
   print(reverse_string)
   if reverse_string==string_name:
      print("palindrome")
   else:
    print("Not a Palindrome")
is_palindrome(string_name)

# Task #2
# Sum of Digits: Create a function that calculates the sum of the digits of a positive integer.
# n = 12345
# sum = 15

digits=input("enter the sum of num:")
total=0
for i in range(0,len(digits)):
    total=total+int(digits[i])
print(total)
