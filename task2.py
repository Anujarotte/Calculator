#arithmaticoperator
a=int(input("Enter Number---> "))
b=int(input("Enter NUmber---> "))
def add(a,b):
    return a+b
def substarct(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    return a/b
select=int((input("Select the mode--->")))
if select==1:
    print('a''+''b''=',add(a,b))
elif select==2:
    print('a''-''b''=',substarct(a,b))
elif select==3:
    print('a''*''b''=',multiply(a,b))
elif select==4:
    print('a''/''b''=',divide(a,b))            
else:
    print("invalid")
#Define a custom sorting key function
def last_character(string):
    # Return the last character of the string
    return string[-1]

