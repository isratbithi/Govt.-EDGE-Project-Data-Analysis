'''age=int(input("Enter your age: "))
if(age>=0 and age<13):
    print("Child")
elif(age>=13 and age<20):
    print("Teneger")
elif(age>=20 and age<60):
    print("Adult")
else:
    print("Senior citizen")

#leap year
y=int(input("Enter year : "))
if((y%4==0 and y%100!=0) or (y%400==0)):
    print("Leap year")
else:
    print("Not leap year")

#mini calculator
num1=int(input("Enter 1st number : "))
num2=int(input("Enter 2nd number :"))
op=input("Enter operator +,-,*,/,% :")
if(op=='+'):
    result=num1+num2
    print(result)
elif(op=='-'):
    result=num1-num2
    print(result)
elif(op=='*'):
    result=num1*num2
    print(result)
elif(op=='/'):
    result=num1/num2
    print(result)
elif(op=='%'):
    result=num1%num2
    print(result)
elif(op=='**'):
    result=num1**num2
    print(result)
elif(op=='//'):
    result=num1//num2
    print(result)
else:
    print("Invalid")
    
bio="I live in kushtia"
print(bio.find("kushtia"))
print(bio.replace("kushtia","dhaka"))
print(bio.upper())
print(bio.lower())
print(bio[::-1])
print(bio.split())


#calculate grade
marks=float(input("Enter marks 0-100: "))
if(marks>=80):
    print("A+")
elif(marks<80 and marks>=75):
    print("A")
elif(marks<75 and marks>=70):
    print("A-")
elif(marks<70 and marks>=65):
    print("B+")
elif(marks<65 and marks>=60):
    print("B")
elif(marks<60 and marks>=55):
    print("B-")
elif(marks<55 and marks>=50):
    print("C")
elif(marks<55 and marks>40):
    print("D")
else:
    print("Invalid marks")
    
a=76
b=70
def dif(x,y):
    print(id(x))
    print(id(y))
    return x-y
print(dif(a,b))
print(id(a))
print(id(b))
#finde even number
i=int(input("Enetr value : "))

while i<100:
    print(i)
    i+=2
    
#find multiplication
n=int(input("Enter value : "))
i=1
while i<=10:
    print(f"{n} X {i} = {n*i}")
    i+=1'''
#find factorial number
n=int(input("Enter value : "))
i=1
ans=1
while (i<=n):
    ans*=i
    i+=1
print(ans)

    