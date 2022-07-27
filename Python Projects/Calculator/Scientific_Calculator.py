# Project Name _ Scientific Calculator
import  math

def Add(x,y):
    print(f'Sum of {x} and {y} is {x+y}')
def Squareroot(x):
    print(f'Squareroot of {x} is {math.sqrt(x)}')
def Subtraction(x,y):
    print(f'Sum of {x} and {y} is {x-y}')
def Division(x,y):
    print(f'Sum of {x} and {y} is {x/y}')
def Multiplication(x,y):
    print(f'Sum of {x} and {y} is {x*y}')

a=input('Enter which Operation You Wants to perform \n 1) Add \n 2) Subtraction \n 3) Multiplication \n 4) Division \n 5) Squareroot \n ')
if a=='Add':
    x=int(input())
    y=int(input())
    Add(x,y)
elif a=='Squareroot':
    x=int(input())
    Squareroot(x)
elif a=='Subtraction':
    x=int(input())
    y=int(input())
    Subtraction(x,y)
elif a=='Division':
    x=int(input())
    y=int(input())
    Division(x,y)
elif a=='Multiplication':
    x=int(input())
    y=int(input())
    Multiplication(x,y)

