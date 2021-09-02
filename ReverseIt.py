#Reverse text given as input

def reverse(string):
    string = "".join(reversed(string))
    return string

def palindrome(string):
    lowerString = string.lower()
    if lowerString == reverse(lowerString):
        return "yes"
    else:
        return "no"

myString = input()    

vCount = 0
cCount = 0
v = []
c = []

vowels="aeiouAEIOU"
for letter in myString:
    if letter in vowels:
        #print (letter)
        vCount = vCount + 1
        v.append(letter)
    elif letter not in vowels:
        cCount = cCount + 1
        c.append(letter)

print("Original text: " + myString)
print("Reversed text: " + reverse(myString))
print("Palindrome?  : " + palindrome(myString))
print("Vowels       :",vCount,v)
print("Consonants   :",cCount,c)

#might have made more sense to use a dictionary instead of a list and just count what was in there?
