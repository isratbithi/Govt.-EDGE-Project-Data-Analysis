'''#list data type

my_list=[1,2,3,4,5]
sum=0
for item in my_list:
    sum+=item
    
print(sum)
#sort vs sorted

my_list=[3,1,4,1,5,9,2,6,5]
my_list.sort(reverse=True)
print(my_list)

my_list=[3,1,4,1,5,9,2,6,5]
sorted_list=sorted(my_list)
print(sorted_list)
print(my_list)

list=[]
for i in range(1,20):
    if i%2==0:
        list.append(i**2)
print(list)

square_list=[i**2 for i in range(11) if i%2==0]
print(square_list)

words=["hello","world","python"]
length=[len(word) for word in words]
print(length)

#Extract Uppercase Character from a string and Make a list
str="ISraT JaHan Bithi"
list1=[]
list=[ list1 for list1 in str if list1.isupper()]
print(list)
str="ISraT JaHan Bithi"
list1=[]
list=[ list1 for list1 in str.lower() if list1 in "aeiou"]
print(list)
'''

#tuple data type
my_tuple=(1,'a','a',2,3)
x=my_tuple.count('a')
print(x)

print(my_tuple.index(2))



