import itertools
#String is immutable i.e cannot be changed
str="Harry"
print(str[1:3])      #including start and exluding end
print(str[-4:-2])    #= print(str[-4:len(str)-2])

str1="GEEKSFORGEEKS"
print(len(str1))
print(str1[12:1:-2]) #= print(str1[len(str1)-1:len(str1)-12:-2])

str2="Aditya"
print(str2[-1:-6:-1])

print("".join(itertools.islice(str2,0,6)))

#STRING METHOD

a="Aditya raj"
print(a.endswith("ya",0,7))
print(a.replace("a","A"))
print(a.capitalize())
print(a.find("ya"))
print(a.index('a'))
print("string is alphnumeric",a.isalnum())
print("String is alpha",a.isalpha())
print("string is lower case",a.islower())
print("Is string contains white space",a.isspace())
print("is string start with A",a.startswith('A'))
print("Convert case to uppercase to lower case and lower to uppercaser",a.swapcase())
print("Convert each word of string to upper case",a.title())

