'''try:
    age=int(input("Please type in your age: "))
except ValueError:
    age=-1
if age>=0 and age<=150:
    print("That is a fine age")
else:
    print("That is invalid age")
#type error
try:
    result="Hello" + 42

except:
    print("Type Error")

#ZeroDivisionError
try:
    result=10/0
except ZeroDivisionError as e:
    print("ZeroDivisionError occurred: ",e)

#Calculating factorials with
try:
    num=int(input("Enter any number: "))
    if num<=0:
        raise ValueError
    i=1
    ans=1
    while (i<=num):
        ans*=i
        i+=1
    print(ans)
except ValueError as e:
    print("Invalid Number")
    print(e)

print("Sucessfully Completed")


#Exercise:2...Password Verification with Exception Handling
try:
    password=input("Enter Your Password: ")
    if len(password)<8:
        raise ValueError("Password must be at least 8 characters long.")
    if not any(char.isupper() for char in password):
        raise ValueError("Passord must content at least one uppercase.")
    if not any(char.isdigit() for char in password):
        raise ValueError("Password must contain at least one digit.")
except ValueError as e:
    print("Invalid Password:",e)
else:
    print("Password verified successfully.")
'''
#Exercise 1: Extract NUmbers from a given string
import re
text="apple123banana456cherry"
pattern=r"\d+"
new_text=re.findall(pattern,text)
print(new_text)


#Exercise 2:Extract Date from a String with Error Handling
import re
try:
    text="Birthday 2000-12-10"
    pattern=r"\d{4}-\d{2}-\d{2}"
    match=re.findall(pattern,text)
    if len(match)<=0:
        raise ValueError("Invalid date of birth.")
    else:
        print(match)
except ValueError as e:
    print(e)

except Exception as b:
    print(b)

print("Successfully") 