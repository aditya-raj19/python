#required a and b
def addition(a,b):
 print(a+b)

#a and b is option
def sub(a=4,b=6):
 print(a-b)

#convert argiments into tuple
def average(*number):
 print(type(number) ,number)

#pass the function
def checkpass():
 pass

#convert argument into dictionary
def dict(**d):
 print(type(d),d)

addition(5,6)
sub()
sub(a=7,b=5)
average(2,3,4,4)
dict(aditya=4,raj=7)
checkpass()