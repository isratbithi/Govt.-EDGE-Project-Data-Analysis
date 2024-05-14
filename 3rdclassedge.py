'''#rise statement
try:
    roll=int(input("Enter your roll: "))
    if roll<=0:
        raise ValueError
    print("Your roll is ",roll)
except  ValueError as e:
    print("Invalid Roll")
    print(e)
print("Successfully completed")

#string vs row string
string="C:\path\to\file.txt"
print(string)

raw_string=r"C:\path\to\file.txt"
print(raw_string)'''

#Regex Function
import re
text="The quick brown fox jumps over the lazy dog."
pattern=r"Fox"
match=re.search(pattern,text,re.IGNORECASE)
print(match)

import re
text="apple,banana,cherry,date,banana,elderberry"
pattern=r"banana"
matches=re.findall(pattern,text)
print("Occurrence of 'banana' :",matches)


import re
text="The quick brown fox jumps over the lazy dog."
pattern=r"fox"
match=re.sub(pattern,"cat",text)
print("Original text is: ",text)
print("After replacement text is:",match)

import re
text="apple, banana; cherry-date"
pattern=r"[,;\s-]+"
tokens=re.split(pattern,text)
print("Tokens:",tokens)
import re
text="apple123banana456cherry789date"
pattern=r"\d+"
tokens=re.split(pattern,text)
print("Tokens: ",tokens)

import re
text="The event is scheduled for 2024-05-10."
pattern=r"\d{4}-\d{2}-\d{2}"
match=re.search(pattern,text)
print(match)

import re
text="abcdefghijklmngou"
pattren=r"[aeiou]"
ans=re.findall(pattren,text)
print(len(ans))
