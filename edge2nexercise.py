'''#Exercise 1: String Reversal

name=input("Enter any string : ")
revers_name=" "
length=len(name)-1
while length>=0:
    revers_name+=name[length]
    length-=1
print(revers_name)

#Exercise :2 Vowel Counter

name=input("Enter any string : ")
vowels="aeiou"
count=0
index=0

while index<len(name):
    if name[index].lower() in vowels:
        count+=1
    index+=1
print(count)

#Program to print all odd numbers between 1and 10, skipping even numbers

num=1
while num<=10:
    if num%2==0:
        num+=1
        continue
    print(num)
    num+=1

#Program to find the first even number in a sequence of numbers
i=1
while True:
    if i%2==0:
        print("The first even number is :",i)
        break
    i+=1
 #use of break and continue
i=1
while i<=10:
    if i==3:
        i+=1
        continue
   
    print(i)
    i+=1
    
#types of writing for loop
numbers="ICT DEPT,KUSHTIA"
for num in numbers:
    print(num)

#range function.......prime or not prime
num=int(input("Enter any number : "))
is_prime=True
n=num//2+1
for i in range(2,n+1):
    if num%2==0:
        is_prime=False
        break

if is_prime:
    print("Prime")
else:
    print("Not prime")

#define the ranhge of numbers for the multiplication table

start=1
end=10
#Outer loop to iterate over each number for multiplication 
for i in range(start,end+1):
    #Inner loop to iterate over the multiplication of the current number
    for j in range(1,11):
        result=i*j
        print(f"{i} X {j} = {result}")
#Type error 
try:
    result="Hello" + 42 #Trying to concatenate a string and integer directly
except TypeError as e:
    print("TypeError occurred:",e)'''
#index error
try:
    my_list=[1,2,3]
    print(my_list[3])
except IndexError as e:
    print("IndexError Occurred: ",e)
