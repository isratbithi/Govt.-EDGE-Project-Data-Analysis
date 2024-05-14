'''#check palindrome

str=input("Enter any string: ")
str1=str[::-1]
if str==str1:
    print("This string is palindrome..")
else:
    print("This string is not palindrome..")'''

#Exercise 1: Calculating Factorials with Exception Handling
try:
    num = int(input("Enter a positive integer: "))
    if num < 0:
        raise ValueError("Input must be a positive integer")
    
    factorial = 1
    for i in range(1, num + 1):
        factorial *= i
    
    print(f"The factorial of {num} is {factorial}")
except ValueError as ve:
    print(f"Error: {ve}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
