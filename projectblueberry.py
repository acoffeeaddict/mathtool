#greetings
print("Welcome! To start, enter the following values of you 1st fraction. Than, press the enter key!")
a = float(input ("Please enter your numerator"))
b = float(input("Please enter your denominator "))
c=a/b
print("Please enter the numerator and denominator for the second fraction")
d = float(input("Please enter your numerator "))
e = float(input("Please enter your denominator for the second fraction "))
lemon = (input("To get your answer, please select a following option.([Z].Add [X]Subtract [Y]Multiply [W]Divide "))
if lemon in ['Z,z']:
    print(c+f)
if lemon in ['X,x']:
    print(c-f)
if lemon in ['Y,y']:
    print(c*f)
if lemon in ['W,w']:
    print(c/f)
f=(d/e)
q=c*f
print(f)
